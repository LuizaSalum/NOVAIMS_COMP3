<h1>NOVAIMS COMP 3 Final Project: Lolly Locket's Dog Chase</h1>
<p><img alt="Lolly Locket's Dog Chase Start Screen" src="https://github.com/LuizaSalum/NOVAIMS_COMP3/blob/main/images/interface/start.png"/></p>
<p>Every element of the game was drawn using Clip Studio Pro. No AI tool was used for any image. We strongly oppose the use of AI-generated images since most of these generators are fed with human-created art without proper authorisation (To learn more about it, watch: <a href="https://youtu.be/9xJCzKdPyCo?si=QRO3VLsTQcFZI51N">The AI Art Apocalypse</a> by Hello Future Me). Everything was based on the "Polly Party Pickup" game from 2007 <a href="https://pollypocket.fandom.com/wiki/Polly_Party_Pickup">(Wiki)</a> and we have no interest in commercializing this project.</p>
<h2>Group Members</h2>
António Manuel Ferreira dos Santos - 20221966<br>
Brenda Montenegro Pontremoli Lima - 20221865<br>
Maria Luiza Salum Alves Corrêa - 20221902
<hr>
<h2>Project Description</h2>
<p>As our final assignment for our Computation 3 Course, we were asked to use the obtained knowledge about Object-oriented Programming (OOP) to complete the implementation of a Car Racer game using Pygame. The base requirements were to implement two mandatory power-ups, one that slows down traffic and another that makes the player(s) invincible, two optional power-ups of our choice, and a multiplayer option. Also, we were requested to improve the UI, add instructions explaining how to play and how each power-up works, and add functional limitations to make the game operational.</p>
<h3>Technologies Used</h3>
<ul>
    <li>Python Language</li>
    <li>Pygame Library</li>
    <li>Python Random Module</li>
    <li>Abstract Base Classes</li>
</ul>
<h3>Game Story</h3>
<p><em>Our friend <strong>Lolly (Player 1)</strong> was hanging out with her <strong>Bestie (Player 2)</strong> in the local park, playing with her dog, when a sudden noise scared the poor thing! The puppy started running and escaped, so now Lolly needs help rescuing her baby!</em></p>
<p>In the Home Screen, it's explained that Lolly moves with WASD and Bestie with the Arrow Keys.</p>
<p>Win Scenario: <em>The player accepts the phone call and finds out that Lolly's puppy was brought to the <strong>Local Vet Clinic</strong> by a good samaritan, and they were able to contact Lolly thanks to the fact that the dog was chipped!</em></p>
<h3>Requirements Met</h3>
<ul>
    <li>Created 8 Power-Ups (With different probabilities, durations and cooldowns)
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
    <li>Created Different Lolly/Cars Options
        <ol>
            <li>Pink: Extra power-up duration, less power-up cooldown</li>
            <li>Blue: Faster car, less HP</li>
            <li>Purple: More HP, slower</li>
        </ol>
    </li>
    <li>Created a New Interface
        <ol>
            <li>Press ESC on the game screen to open the Pause Menu, and on the other screens to open the Main Menu</li>
            <li>Start/Home Screen: Can open Single-player, Multiplayer and Credits screen (has an exit button)</li>
            <li>Single-player Screen: Can open the Player 1 (Lolly) Customisation, Difficulty (Dog) Selection, and Power Up List screens</li>
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
            <li>Added mask collision between players, players and traffic, and players and power-ups </li>
        </ol>
    </li>
</ul>
<hr>
<h2>How to Install and Run the Project</h2>
<ol>
    <li>Download the ZIP File (Code -> Download ZIP)</li>
    <li>Extract the ZIP File</li>
    <li>Open the folder with the editor of your choice (e.g. Pycharm, Visual Studio Code)</li>
    <li>Run main.py to play the game</li>
</ol>
<p><em>Remember to have Pygame installed.</em></p>
<hr>
<h2>How to Use the Project</h2>
<h3>Images and Sounds</h3>
<p>Every image is located in the "images" folder, and every sound is located in the "sounds" folder.</p>
<h3>Code</h3>
<p>The code is divided into five files:
<ul>
    <li>main.py: Where you can run the game</li>
    <li>interface.py: Where you can find the code for the interface before the actual race</li>
    <ul>
        <li>Start/Home Screen</li>
        <li>Credits</li>
        <li>Single-player Customisation</li>
        <li>Multiplayer Customisation</li>
        <li>Dog Selection</li>
        <li>Lolly Selection</li>
        <li>Bestie Selection</li>
        <li>Power-Ups List</li>
        <li>Menu</li>
    </ul>
    <li>game.py: Where you can find the code for everything that happens in the race</li>
    <ul>
        <li>Single-player Race</li>
        <li>Multiplayer Race</li>
        <li>Countdown (before the race)</li>
        <li>Game Over</li>
        <li>Pause Menu</li>
        <li>Active Power-Ups Function</li>
        <li>Active Power-Ups Bar</li>
        <li>Victory</li>
    </ul>
    <li>car.py: Where you can find the code for the different cars in the game</li>
    <ul>
        <li>Car (Parent Class)</li>
        <li>PlayerCar</li>
        <li>TrafficCar</li>
    </ul>
    <li>power_up.py: Where you can find the code for every power-up in the game</li>
    <ul>
        <li>PowerUp (Parent Class)</li>
        <li>BestiesInHarmony</li>
        <li>GalPalRebirth</li>
        <li>TangledTwist</li>
        <li>SissyThatWalk</li>
        <li>DivaDefiance</li>
        <li>GlamorousGrowth</li>
        <li>FrostyFrenzy</li>
        <li>ToyTransforminator</li>
    </ul>
</ul>
<hr>
<h2>Unresolved Issues</h2>
<p>Sometimes the victory story is not displayed; The game freezes in the "..." part and unfreezes in the victory screen. We tried changing the delay to clock tick and things like that, but nothing seemed to work.</p>
<p>Sometimes the "Besties In Harmony" power-up stops moving out of nowhere and disappears after a while. We don't know why or how this is happening.</p>
