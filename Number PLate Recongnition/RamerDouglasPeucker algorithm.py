#RamerDouglasPeucker algorithm

#https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm#:~:text=The%20Ramer%E2%80%93Douglas%E2%80%93Peucker%20algorithm,algorithms%20developed%20for%20Cartographic%20generalization.
#https://www.youtube.com/watch?v=lzqTD0JWwhY


from math import sqrt

#each paramter start, end, point is in the form [x,y]
def point_line_distance(start,end, point):

    
    #both point are same , now just distance between two point formula
    if start==end:
        #  sqrt( (x2-x1)^2 + (y2-y1)^2 )
        return sqrt( (end[0]- start[0])**2 + ( end[1] - start[1] )**2 )
        
    # mathematical formula
    else:
        
        num=abs( (end[0] - start[0])*(start[1]- point[1]) - (start[0]-point[0])*(end[1]-start[1]) )
        denom=sqrt( (end[0]-start[0])**2 + (end[1] - start[1])**2)
        
        return num/denom

        
#we dont have refrence concept in python so  to store in resultanat arraay in python, so we return list,     
def RDP(points, epsilon):

    
    start=0 ;
    end=len(points)-1 ; 
   
    maxDist=0.0 ;
    index=0;
    
    #perpendicular shortest distance to the line between start and end 
    for i in range(1,end):
       
        dist=point_line_distance(points[start],points[end],points[i])
        
        if(dist>maxDist):
            index=i
            maxDist=dist
          
        
    result=[]
    
    if maxDist >= epsilon:  
        #both the list of list are added to give result
        result=RDP(points[:index+1],epsilon)+RDP(points[index:],epsilon)

        
    #no need to approximate
    else :
        result=[points[start][0],points[end][0]]
        
    return result
      
if __name__=="__main__":
    
    
    points=[[1, 2], [3, 4], [4, 5], [6, 7]]
    epsilon=0.1
    approxPoints=RDP(points,epsilon)
    print(len(points))
    print(len(approxPoints))
    
