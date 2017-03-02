
<h1>Tokens</h1>
<h3><p>The following describes the problem that the alogirthm I implemented solves. the print out determins the sequence of choices that should be made during any given time in the game</p></h3>
<br>You’re playtesting a new boardgame from one of your friends in the Game Design major, and they want your help to figure out the optimal strategy. 
<br>The game has n rounds and in each round 1 ≤ i ≤ n you must acquire si tokens. There are two possible ways to acquire tokens in round i:
<ul><li>A Spend r dollars per token, so r · si in total, to acquire all token of round i.</li>
<li>B Spend C dollars to acquire the tokens of round i and of the next 3 rounds, independently of how many there are.
(If you do this in round i, then your next choices concern rounds i + 4 and greater).</li></ul>
<br>Example. Suppose r = 1, C = 40, and the sequence of si is 11, 9, 9, 12, 12, 12, 12, 9, 9, 11. 
<br>Then the cheapest way to acquire all the tokens is to choose action A for the first three rounds, then action B once, and then action A for the final three rounds.
<br>Give a dynamic programming algorithm for finding the cheapest way to acquire all tokens, given the sequence s1 , s2 , . . . , sn .
<br>You must describe not only how you determine the value of the optimal sequence of actions, but also the sequence of actions itself.
