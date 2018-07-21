# Great Circle Routes
Problem Description
It is well known that the shortest path between two points on the surface of the earth (assumed to be a perfect sphere of radius 6400 km) is a great circle route. To get this, draw the circle (on the surface of the earth) that goes through the two points which is centred at the centre of the earth. The shorter arc of the circle between the two points is the shortest distance. In the figure below, the solid circle represents the earth (assumed to be a sphere), with centre O. There are two points X and Y on the surface (whose positions can be specified by a latitude and longitude). The dotted line represents a circle on the surface of the earth, with centre O. The length of the arc of the circle between X and Y is the great circle distance, which is the shortest distance between the two points while travelling on the surface.

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@36cbfd2b:image1.png

A traveler wishes to accomplish a complex itinerary, going from point to point. Each point is specified by its latitude in degrees north or south, and its longitude in degrees East or West. The objective is to calculate the total distance travelled by the traveler as he goes from point to point in order, if he travels by the shortest distance between any two points.

Constraints
N<=10

Input Format
Line 1 contains N, the number of points the traveler wishes to travel between.

The next N lines each contain two comma separated strings specifying the latitude and longitude of the point in degrees. The latitude string consists of a non-negative integer (representing the latitude of the point) followed by N or S to indicate north or south. (A point on the equator will be represented by 0N). The longitude string will consist of a non-negative integer representing the longitude of the point in degrees, followed by E or W to specify East or West. For longitudes where it does not matter (such as 0 and 180) the longitude will always be specified as E. The north and south poles will be deemed to have 0 longitude

Output
The output should be one line that specifies the distance travelled by the traveler to the nearest integer. The traveler will travel from one point to the next in order.


Explanation
Example 1

Input

3

0N,1W

0N,179E

90N,0E

Output

30159

Explanation

There are 3 points. The first point is one on the equator, and 1 degree West. The second point is also on the equator, and 179 degrees East. The third point is the north pole.

The great circle passing through the first two points is the equator (as its centre is the centre of the earth). As the difference in longitudes (taking the fact that one is E and one is W) is 180 degrees. Hence this distance is half the circumference of the earth, or 0.5 * 2* π *6400=6400 π.

To find the distance between the second and the third point, we note that the longitude 179 degrees East passes through the north pole and is a great circle. The angle subtended at the centre of the earth by the two points is 90 degrees, and hence the distance is (1/4) of the circumference of the circle, or (0.25)*2*π*6400, or 3200π.

The total distance travelled is 9600π or 30159 (to the nearest integer). This is the output.

Example 2

Input

3

0N,47E

45N,47E

45S,47E

Output

15080

Explanation

As the first and second points are on the same longitude, the longitude is the great circle that passes through them. The angle subtended at the centre of the earth is 45 degrees, as that is the difference in the latitudes. Hence the great circle distance is (1/8) of the circumference of the circle, or (0.125*2*π*6400)=1600π

The second and third points are also on the same longitude, and the angle subtended at the centre of the earth is 90 degrees. Hence the distance between the points is (1/4) of the circumference of the circle. The distance is (0.25)*2*π*6400, or 3200π.

The total distance travelled is 4800π, or 15080. This is the output.
