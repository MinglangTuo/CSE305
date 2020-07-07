# Ant colony algorithm optimizes bus routes

## Background
Traffic congestion in Suzhou has been increasing in recent years. Thus it’s beneficial to develop a replaceable transport system, such as trams, to promote urban development.
As well as the different tram stations, generating one of the main tasks to be solved by logistics companies: the design of the tram route to optimization. Recently, one valid
solution was proposed by several commercials for route planning. However, the cost of these applications is crucially high because of the multi-variable optimization including the requirement of passengers, the distance of stations and the maximum capacity of tram which makes the acquisition of application tough to afford. 

## Core-idea
In this project, an optimize route design algorithm is developed for those route deciders to design more efficient routes based on the requirements. In order to generate the final optimize routes, the algorithm allows users to enter information about distance stations, passenger requirements and the number of required routes. In this algorithm, the core problem can be regared as traveling salesman problem and one of the heuristic approachs named ant-colony algorithm has been improved based on a-star algorithm and utilized, which is the core idea of algorithm to optimize the routes. Furthermore, this reprot also discusses how the final solutions are influenced by the different ant-colony parameters based on different range of tramstations and compares the effect between the original ant-colony algorithm and enhanced ant-colony algorithm.

## DataSet
The dataSet file contains some csv files, which simulate the random 20 stations and 30 passengers, random 30 stations and 10 passengers, 40 stations and 10 passengers in the two-dimension coordinates.  

## Code
The visualization Implementation contains the OpenGL file.  

The plot Implementation contains the GGplot2 file.  

The algorithm Implementation contains the Enhanced-Ant-Colony-algorithm.  

## Mathematical formula  

The A* algorithm as a new heuristic method for finding the path which is completely different from the uniform-cost search algorithm like dijkstra algorithm. It can continuously estimate the distance from the initial point to the end point in the tree or graph in each step. Then, the best optimize path will be selected during the each step. Hart et al. (1968) extended the Dijkstra algorithm (Dijkstra, 1959) to propose the A* algorithm. The A* algorithm was used in lots of dimensions. For example, game units in Starcraft go to find the path, which is formally done using the A* algorithm over and over again,allowing units to find the path to the targer you mouse clicked on. The core principle of A* algorithm can be shown in the following formula:  
**F(n) = G(n) + H(n)**  

Another heuristic algorithm is ant-colony-optimize algorithm, which is based on the simulation of the ant-colony looking for food to find the optimal path. In the early 1990s,
M. Dorigo and colleagues discover and create the ant colony optimization (ACO) as an original nature-inspired metaheuristic for solving hard combinatorial optimization (CO) problems. According to the observation and research of entomologists, the ants in the biological world have the ability to find the shortest path from their nest to the food
source without any visible hint. Meanwhile, they can change the shortest path depends on the change of environiment, adaptively search for new path and generate new choices. The reason is the pheromones which can be regard as the special secretions in the paths. It causes that the ants are able to detect and influence their subsequent movements. For
example, with ants passing along some paths more and more, the rate of pheromone on these paths becomes more greater which leads to the subsequent ants more likely to choose
the paths. The process of selection is known as ant autocatalytic behavior.  
As for the formula of RouteSelection, it represents the probability for the antk choose the next random stationj from stationi. It’s like this:  
<img src ="https://github.com/MinglangTuo/CSE305/blob/master/%E5%9B%BE%E7%89%871.png" width ="200" height = "100">  
• m: the total number of ants.  
• k: the ant is exploring in the stations, whose serial number is k. (1<k<m)  
• i: the current station for the ant k.  
• j:the adjacent stations for the current station.  
• τij : the pheromone of edge that is from station i to station j.  
• ηij : the visiablity of edge that is from station i to station j. In addition, the longer  
the road, the less visibility in the road.  
• Λ: the station set which is adjacent to the current station.  
• α: the parameter factor.  
• β: the parameter factor.  
As for the formula of PheromoneUpdate, the function is updating the pheromone in each iteration. It’s like this:  
<img src ="https://github.com/MinglangTuo/CSE305/blob/master/%E5%9B%BE%E7%89%872.png" width ="200" height = "100">  
• n: the total times for m ants to walk athrough all the stations.  
• τ_ij (n): the pheromone of edge between the station i and station j in the previous iteration.  
• τ_ij (n + 1): the pheromone of edge between the station i and station j in the current iteration.  
• ∆τ_k_ij : after this iteration, the ant k remains the pheromone in the edge between the station i and station j.  
• ρ: Evaporation rate (0<ρ<1)  

## Test and Results
There are three sub algorithm for the enhanced ant-colony algorithm.  
1.Bus-Busy-Enhance Algorithm  
<img src ="https://github.com/MinglangTuo/CSE305/blob/master/Picture/pic1/1.png" width ="200" height = "200">
<img src ="https://github.com/MinglangTuo/CSE305/blob/master/Picture/pic1/2.png" width ="200" height = "200">  
<img src ="https://github.com/MinglangTuo/CSE305/blob/master/Picture/pic1/3.png" width ="200" height = "200">
<img src ="https://github.com/MinglangTuo/CSE305/blob/master/Picture/pic1/4.png" width ="200" height = "200">   

2.Ant-Colon Algorithm  
<img src ="https://github.com/MinglangTuo/CSE305/blob/master/Picture/pic2/1.png" width ="200" height = "200">
<img src ="https://github.com/MinglangTuo/CSE305/blob/master/Picture/pic2/2.png" width ="200" height = "200">   
<img src ="https://github.com/MinglangTuo/CSE305/blob/master/Picture/pic2/3.png" width ="200" height = "200">
<img src ="https://github.com/MinglangTuo/CSE305/blob/master/Picture/pic2/4.png" width ="200" height = "200">    

2.Cut-lines Algorithm    
<img src ="https://github.com/MinglangTuo/CSE305/blob/master/Picture/pic3/1.png" width ="200" height = "200">
<img src ="https://github.com/MinglangTuo/CSE305/blob/master/Picture/pic3/2.png" width ="200" height = "200">  
<img src ="https://github.com/MinglangTuo/CSE305/blob/master/Picture/pic3/3.png" width ="200" height = "200">
<img src ="https://github.com/MinglangTuo/CSE305/blob/master/Picture/pic3/4.png" width ="200" height = "200"> 


