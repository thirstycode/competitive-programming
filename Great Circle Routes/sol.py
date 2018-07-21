from math import sin, cos, sqrt, atan2, radians

n = input()
n = int(n)
points = []
for i in range(0,n):
	lat,lon = input().split(',')
	points.append([lat,lon])
new_points = []
for i in range(0,len(points)-1):
	lat_old,lon_old = points[i]
	lat_new,lon_new = points[i+1]
	if lat_old[-1:] == 'N':
		lat_old = float(lat_old[:-1])
	else :
		lat_old = -float(lat_old[:-1])
	if lon_old[-1:] == 'E':
		lon_old = float(lon_old[:-1])
	else:
		lon_old = -float(lon_old[:-1])
	if lat_new[-1:] == 'N':
		lat_new = float(lat_new[:-1])
	else :
		lat_new = -float(lat_new[:-1])
	if lon_new[-1:] == 'E':
		lon_new = float(lon_new[:-1])
	else:
		lon_new = -float(lon_new[:-1])
	new_points.append([[lat_old,lon_old],[lat_new,lon_new]])
# print(new_points)
earth_radius = 6400
ans = 0
for point_jodi in new_points:
	lat1 = radians(point_jodi[0][0])
	lon1 = radians(point_jodi[0][1])
	lat2 = radians(point_jodi[1][0])
	lon2 = radians(point_jodi[1][1])
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))
	distance = earth_radius * c
	# print(distance/pi)
	ans += distance
	
print(int(round(ans)))
