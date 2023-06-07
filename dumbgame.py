from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def start():
    # This is the starting point of the game (Hallway). 
    # Add your description of the hallway and links to other rooms.
    return '''
    You find yourself in a mysterious mansion and you are locked in!
    You are currently in the hallway. There are three doors, each leading to a different room:
    <ul>
        <li><a href='{}'>Library</a></li>
        <li><a href='{}'>Kitchen</a></li>
        <li><a href='{}'>Cellar</a></li>
    </ul>
    '''.format(url_for('library'), url_for('kitchen'), url_for('cellar'))
    pass

@app.route('/library')
def library():
    return''' After long consideration you decide to procced towards the library. as you walk in you see several large bookshelfs filled with millions 
    of book and a red door marked do not open. you can either take a second and read a book.,go through the red door or go back <ul>
        <li><a href='{}'>red door</a></li>
        <li><a href='{}'>read</a></li>
        <li><a href='{}'>go back</a></li>
    </ul>
    '''.format(url_for('reddoor'), url_for('read'), url_for('start'))
    pass

@app.route('/reddoor')
def reddoor():
    return'''
    are you dumb it said do not open but yet you decide to open it. well any way you are right you should 
    have went trough the door and see a small room 
    full of weird orbs filled with different fluids some 
    green some red and a small few black you see no other doors you decide to break one of the orbs . which orb do you break?
    <ul>
        <li><a href='{}'>Red</a></li>
        <li><a href='{}'>green </a></li>
        <li><a href='{}'>black</a></li>
    </ul>
    '''.format(url_for('escape'), url_for('green'), url_for('black'))
    pass
@app.route('/green')
def green():
    return'''
    you choose the wrong one a swarm of the undead rise and start to grab at your feet and get draged underground and sufficate to death
    <ul>
        <li><a href='{}'>play again?</a></li>
        
    </ul>
    '''.format(url_for('start'))
    pass
@app.route('/black')
def black():
    return'''
    you died instanly 
    <ul>
        <li><a href='{}'>Play again?</a></li>
    </ul>
    '''.format(url_for('start'))
    pass
@app.route('/read')
def read():
    return'''you died. the room was slowly being filled with poison but that didn't kill you. you died because you tried to get a book but the shelf fell on 
    you and got crushed to death 
    <ul>
        <li><a href='{}'>play again</a></li>
        
    </ul>
    '''.format(url_for('start'))
    pass
@app.route('/kitchen')
def kitchen():
   return''' you enter the kitchen guess you were hungry. you look around and fined scooby snacks on top of a high self. 
   you look around some more and see a basket of fruit and next to it you see another door marked bedroom(clearly some fat as lives here having his bedroom next to the kitchen)
   what do you do?
   <ul>
        <li><a href='{}'>scooby snacks</a></li>
        <li><a href='{}'>fruit basket</a></li>
        <li><a href='{}'>bedroom</a></li><li>
        <a href='{}'>go back</a></li>
        
    </ul>
   '''.format(url_for('snack'),url_for('fruit'),url_for('bed'),url_for('start'))
   pass
@app.route('/snack')
def snack():
   return'''
   you enjoy some scooby snacks what now?
    <li><a href='{}'>fruit basket</a></li>
        <li><a href='{}'>bedroom</a></li><li>
        <a href='{}'>go back</a></li>'''.format(url_for('fruit'),url_for('bed'),url_for('start'))
   pass
@app.route('/fruit')
def fruit():
   return'''
   you forgot you are a gamer and you have never had a fruit in you life and instanly die on contact with the fruit
    <li><a href='{}'>play again?</a></li>
        '''.format(url_for('start'))
   pass
   
@app.route('/bed')
def bed():
   return''' you decide to go to the bedroom. you see a top teir gaming pc. you decide to bootup a game of cod. you play for 2 weeks straight 
   and die because your mum didn't bring you any snacks 
  
        <a href='{}'>play again?</a></li>'''.format(url_for('start'))
   pass
    
@app.route('/cellar')
def cellar():
   return ''' you decide to take the stairs down to the cellar and check it out but ,you being the idiot you are forgot to tie your shoe laces and fall down the stairs
   but you only broke your leg. where do you do 
    <li><a href='{}'>cry</a></li>
        <li><a href='{}'>crawl to nearset door</a></li>
        
    '''.format(url_for('cry'), url_for('crawl'))
 
   pass
@app.route('/cry')
def cry():
   return'''
   you decide to cry for a bit. but you are to loud and a wolf hears you it decides you look "quite nice to eat" and procceeds to eat you  
       
        <a href='{}'>die</a></li> '''.format(url_for('start'))
   pass

   
@app.route('/crawl')
def crawl():
   return'''you start to crawl but .... im to lazy to finish this ....... an anvil falls on you I guess
    
        <a href='{}'>play again?</a></li>'''.format(url_for('start'))
@app.route('/escape')
def escape():
  return'''
  wow you managed to escape .I guess you are good for something, nothing important though. '''
  pass
    
if __name__ == '__main__':
 app.run(debug=True)