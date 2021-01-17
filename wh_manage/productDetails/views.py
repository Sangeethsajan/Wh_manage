# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import productForm, pathForm, OrderForm
from django.shortcuts import render,redirect,render_to_response
import math

# Create your views here.
def product_list(request):
    return render(request,"productDetails/product_list.html")

def product_order(request):
    if request.method == "GET":
        form = OrderForm()
        return render(request,"productDetails/product_order.html",{'form': form})
    else:
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/product/list/')

def product_form(request):
    if request.method == "GET":
        form = productForm()
        return render(request,"productDetails/product_form.html",{'form': form})
    else:
        form = productForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/product/list/')

def product_delete(request):
    return

def product_path(request):
    if request.method =="GET":
        form = pathForm
        return render(request,"productDetails/product_path.html",{'form':form})
    else:
        form = pathForm(request.POST)
        if form.is_valid():
            #if form.cleaned_data['rack'] == 5:
            def Dijkstra(graph,source,target):
    
                # These are all the nodes which have not been visited yet
                unvisited_nodes=graph
                # It will store the shortest distance from one node to another
                shortest_distance={}
                # This will store the Shortest path between source and target node 
                route=[] 
                # It will store the predecessors of the nodes
                predecessor={}
                
                # Iterating through all the unvisited nodes
                for nodes in unvisited_nodes:
                    
                # Setting the shortest_distance of all the nodes as infinty
                    shortest_distance[nodes]=float('inf')
                    
                # The distance of a point to itself is 0.
                shortest_distance[source]=0
                
                # Running the loop while all the nodes have been visited
                while(unvisited_nodes):
                    
                    # setting the value of min_node as None
                    min_Node=None
                    
                    # iterating through all the unvisited node
                    for current_node in unvisited_nodes: 
                        
                    # For the very first time that loop runs this will be called
                        if min_Node is None:
                        
                        # Setting the value of min_Node as the current node
                            min_Node=current_node
                            
                        elif shortest_distance[min_Node] > shortest_distance[current_node]:
                            
                        # I the value of min_Node is less than that of current_node, set 
                        #min_Node as current_node

                            min_Node=current_node
                            
                    # Iterating through the connected nodes of current_node (for # 
                    #example, a is connected with b and c having values 10 and 3 
                    # respectively) and the weight of the edges

                    for child_node,value in unvisited_nodes[min_Node].items():

                        # checking if the value of the current_node + value of the edge 
                        # that connects this neighbor node with current_node
                        # is lesser than the value that distance between current nodes 
                        # and its connections
                        if value + shortest_distance[min_Node] < shortest_distance[child_node]:  
                            
                # If true  set the new value as the minimum distance of that connection
                            shortest_distance[child_node] = value + shortest_distance[min_Node]
                            
                    # Adding the current node as the predecessor of the child node
                            predecessor[child_node] = min_Node
                    
                    # After the node has been visited (also known as relaxed) remove it from unvisited node
                    unvisited_nodes.pop(min_Node)
                    
                # Till now the shortest distance between the source node and target node 
                # has been found. Set the current node as the target node 
                node = target
                
                # Starting from the goal node, we will go back to the source node and 
            # see what path we followed to get the smallest distance
                while node != source:
                    
                    # As it is not necessary that the target node can be reached from # the source node, we must enclose it in a try block
                    try:
                        route.insert(0,node)
                        node = predecessor[node]
                    except Exception:
                        print('Path not reachable')
                        break
                # Including the ssource in the path
                route.insert(0,source)
                
                # If the node has been visited,
                if shortest_distance[target] != float('inf'):
                    # print the shortest distance and the path taken
                    print('Shortest distance is ' + str(shortest_distance[target]))
                    print('And the path is ' + str(route))
                    return route
                # Remove the below comment if you want to show the the shortest distance 
                #from source to every other node
                # print(shortest_distance)

            graph = {'a':{'b':5,'c':2},'b':{'c':1,'d':3},'c':{'b':3,'d':7},'d':{'e':7},'e':{'d':9}}
            #Calling the function with source as 'a' and target as 'e'.
            sa = Dijkstra(graph,'a','d')
            print(sa)
            link = ["Hello","Hai"]
            print(sa)
            return render(request,'productDetails/product_path.html',{'sa':sa})
        return redirect('/product/')
