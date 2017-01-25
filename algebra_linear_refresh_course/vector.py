from math import sqrt, acos, pi
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Can not normalize the zero vector'
    CANNOT_COMPUTE_AN_ANGLE_WITH_THE_ZERO_VECTOR_MSG = "Cannot compute an angle with the zero vector"

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)
        except ValueError:
            raise ValueError('The coordinates must be nonempty')
        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        #list comprehennssi
        new_coordinates = [ x+y for x,y in zip(self.coordinates, v.coordinates)]
        #new_coordinates = []
        #n = len(self.coordinates)
        #for i in range(n):
        #   new_coordinates.append(self.coordinates[i] + v.coordinates[i])
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x-y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, c):
        new_coordinates = [ Decimal(c)*x for x in self.coordinates ]
        return Vector(new_coordinates)

    def magnitude(self):
        squares_coordinates = [x**2 for x in self.coordinates]
        sum_coordinates = sum(squares_coordinates)
        return Decimal(sqrt(sum_coordinates))

    def normalized(self):
        try:
            mag = self.magnitude()
            vetor_unit = self.times_scalar(Decimal('1.0')/mag)
            return vetor_unit
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def inner_product(self, vetor):
        x_coordinates_times_y_coordinates = [x*y for x, y in zip(self.coordinates, vetor.coordinates)]
        sum_coordinates = sum(x_coordinates_times_y_coordinates)
        return sum_coordinates

    def dot(self, v):
        return sum( [x*y for x, y in zip(self.coordinates, v.coordinates)])

    def angle_rad(self, vetor):
        owner_magnitude = self.magnitude()
        vetor_magnitude = vetor.magnitude()
        inner_product_vector = self.inner_product(vetor)
        angle = 0
        try :
            cosine_angle = inner_product_vector / (owner_magnitude * vetor_magnitude)
            angle = acos(cosine_angle)
            return angle
        except ZeroDivisionError :
            raise Exception('One or both vectors are equal zero')

    def angle_degrees(self,vetor):
        angle = self.angle_rad(vetor)
        return degrees(angle)

    def angle_with(self, vetor, in_degrees=False):
        try:
            u1 = self.normalized()
            u2 = vetor.normalized()
            angle_in_radians = acos(round(float(u1.dot(u2)),4))
            if in_degrees:
                degrees_per_radian = 180./ pi
                return angle_in_radians * degrees_per_radian
            else :
                return angle_in_radians
        except Exception as e :
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.CANNOT_COMPUTE_AN_ANGLE_WITH_THE_ZERO_VECTOR_MSG)
            else:
                raise e

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance

    def is_parallel_to(self, v):
        return ( self.is_zero() or
                 v.is_zero() or
                 self.angle_with(v) == 0 or
                 self.angle_with(v) == pi )
