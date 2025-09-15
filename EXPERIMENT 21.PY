% planet(Name, DistanceFromSun, Moons)
planet(mercury, 58, 0).
planet(venus, 108, 0).
planet(earth, 150, 1).
planet(mars, 228, 2).

% Example:
% ?- planet(Name, D, B).
% Name = mercury, D = 58, B = 0 ;
% Name = venus, D = 108, B = 0 ...
