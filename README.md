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

## Test and Results



Thanks!
