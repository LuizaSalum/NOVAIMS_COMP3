<h1>NOVAIMS COMP 3 Final Project: Lolly Locket's Dog Chase</h1>
<h2>Group Members:</h2>
António Manuel Ferreira dos Santos - 20221966<br>
Brenda Montenegro Pontremoli Lima - 20221865<br>
Maria Luiza Salum Alves Corrêa - 20221902
<hr>
<br>

<h2>Project Description</h2>
<p>As our final assignement for our Computation 3 Course, we where asked to use the obtained knowledge about Object-oriented Programming (OOP) to complete the implementation of a Car Racer game using Pygame. The base requirements were to implement two mandatory power ups, one that slows down traffic and another that makes the player(s) invincible, two optional power ups of our choice, and a multiplayer option. Also, we were requested to improve the UI, add instructions explaining how to play and how each power up works, and to add functional limitations to make the game operational.</p>
<br>
<p>Requirements Met:</p>
<ul>
    <li>Created 8 Power Ups
        <ol>
            <li>Besties In Harmony (multiplayer only): Players' cars don't collide</li>
            <li>Gal Pal Rebirth (multiplayer only): Eliminated player gets revived</li>
            <li>Tangled Twist (multiplayer only): Players' controls are inverted</li>
            <li>Sissy That Walk: Movement speed boost</li>
            <li>Diva Defiance (mandatory): Invulnerability/Invincibility</li>
            <li>Glamorous Growth: Player grows in size and gets one extra HP (health point)</li>
            <li>Frosty Frenzy (mandatory): Slows down traffic</li>
            <li>Toy Transforminator: Shrinks traffic</li>
        </ol>
    </li>
    <li>Created Difficulties
        <ol>
            <li>Easy: Extra HP and less traffic cars</li>
            <li>Normal</li>
            <li>Hard: Less HP, faster traffic cars, traffic goes both ways</li>
        </ol>
    </li>
    <li>Created Different Cars Options
        <ol>
            <li>Pink: Extra power up duration, less power up cooldown</li>
            <li>Blue: Faster car, less HP</li>
            <li>Purple: More HP, slower</li>
        </ol>
    </li>
    <li>Created a New Interface
        <ol>
            <li>Press ESC in the game screen to open the Pause Menu, and in the other screens to open the Main Menu</li>
            <li>Start/Home Screen: Can open Singleplayer, Multiplayer and Credits screen (has an exit button)</li>
            <li>Singleplayer Screen: Can open the Player 1 (Lolly) Customisation, Difficulty (Dog) Selection, and Power Up List screens</li>
            <li>Multiplayer Screen: Can open the Player 1 (Lolly) Customisation, Difficulty (Dog) Selection, Power Up List, and Player 2 (Bestie) Customisation screens</li>
            <li>Credits Screen: Can go back to the Home Screen</li>
            <li>Main Menu: Can open the Home and Credits screens (has an exit button)</li>
            <li>Pause Menu: Can exit the game</li>
            <li>Game Over: Can restart or exit the game</li>
            <li>Victory: Displays a short story and then the Victory Screen</li>
            <li>Victory Screen: Can restart or exit the game</li>
        </ol>
    </li>
    <li>Created Functional Limitations
        <ol>
            <li>Player can move up and down</li>
            <li>Player can't go out of bounds (out of the road)</li>
            <li>Eliminated Players can't move</li>
            <li>Added mask collision between players, players and traffic, and players and power ups</li>
        </ol>
    </li>
</ul>
<br>
<h3>Game Story</h3>
<p><em>Our friend <strong>Lolly (Player 1)</strong> was hanging out with her <strong>Bestie (Player 2)</strong> in the local park, playing with her dog, when a sudden noise scared the poor thing! The puppy started running and escaped, so now Lolly needs help rescuing her baby!</em></p>
<p>In the Home Screen, it's explained that Lolly moves with WASD and Bestie with the Arrow Keys.</p>
<p>Win Scenario:</p>
<p><em>The player accepts the phone call and finds out that Lolly's puppy was brought to the <strong>Local Vet Clinic</strong> by a good samaritan, and they were able to contact Lolly thanks to the fact that the dog was chipped!</em></p>
<hr>
<br>
<h1> Files Created </h1>
main.py<br>
game.py<br>
car.py<br>
power_up.py<br>
interface.py<br>