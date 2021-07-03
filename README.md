# SavageProject
 
#simple structure of the data flow.

module: Gen.
    input: none
    output: username(lists), list of followers and following for each(sub-lists)
module: AI
    input: all Gen output
    output: usernames(lists), intra-username connection specifying direction
