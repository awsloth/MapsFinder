# Maps wanderer

A project to waste time effectively

## Aim

To waste time by creating a route from point A to B that takes the amount of extra time you have

## How

Using the Google Maps API, nearby 'attractions' can be found, through analysing the paths through
these attractions a route taking the time needed to be wasted can be found and given to the user

### Graphical explanantion

Each route is a tree of the original graph or a tree of a subgraph, such that no attraction is visited twice.
The weights of each arc is found by using Google maps' distance matrix api. The closest route is then found and shown as a route on google maps.
