|
 |
 |
 |
| --- | --- | --- |

#
# Football player roaster formation algorithm

As for the algorithm, I tried using Google to find the solution but still can&#39;t (((

✅ **v0.1** - Here are the basic requirements:

Input variables:

1. Total time to play (e.g. 120 mins)
2. Number of players with their names (e.g. 13)
3. Number of teams (e.g 2)

Output results:

1. Optimal amount of time between &quot;switches&quot;, so that everybody plays ~ the same amount of total time.
2. Roaster of 2 teams for each of the &quot;switches&quot;
3. Each player shall play with as many people in his team as possible - &quot;player rotation&quot;

Use case:

1. User inputs the variables in a form of table, for example
2. User gets roaster of each &quot;switch&quot;, including player names on each team
3. Some debug information may be presented:
    1. Optimal amount of time between &quot;switches&quot;
    2. Number of minutes every player plays (calculated based on formed roaster)
    3. Matrix of each player (x-axis) to each player (y-axis), where the intersection shows amount of minutes that each player shall plays with another player

**Example** :

Switch 1 - min 0-7:
| Player A | Player F |
| --- | --- |
| Player B | Player G |
| Player C | Player H |
| Player D | Player I |
| Player E | Player J |

Switch 2 - min 7-14:
| Player K | Player F |
| --- | --- |
| Player L | Player G |
| Player C | Player H |
| Player D | Player A |
| Player E | Player B |

…

————

✅ **v0.2** - **Goalkeeper changes**

Based on v.0.1 input variables form:

1. Roaster of goalkeepers with timestamps on each team

————

✅ **v0.3** - **Players ranking** affects roaster formation

Introduce new input variables:

1. For each player - ranking shall be introduced
  1. scale: 1,2,3,4,5

Output:

1. Players ranking affects roaster formation so that each team is &quot;balanced&quot; - total amount of &quot;ranking points&quot; between teams deviates as little as possible (e.g. 23\&lt;-\&gt;22)

————

✅ **v0.4** - **Players role** affects roaster

Introduce new input variables:

1. For each player - position
  1. possible values: attack, middle, defense

Output:

1. Players role affects roaster formation so that each team is &quot;balanced&quot; - each team has ~ equal amount of attackers, midfielders &amp; defenders

|
 |
 |
 |
| --- | --- | --- |