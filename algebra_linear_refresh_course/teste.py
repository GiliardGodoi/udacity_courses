from vector import Vector


def teste_soma():
    v1 = Vector([5,5,5])
    v2 = Vector([2, 2, 2])

    v3 = v1.plus(v2)
    print(v3)


def test_magnitude_vetor_unitario():
    v1 = Vector([-0.221, 7.437])
    tamV1 = v1.magnitude()
    print(tamV1)

    v2 = Vector([8.813, -1.331, -6.247])
    print(v2.magnitude())

    v3 = Vector([5.581, -2.136])
    print(v3.normalized())

    v4 = Vector([1.996, 3.108, -4.554])
    print(v4.normalized())

def dot_product_and_angle():
    print('DOT PRODUCT \n\tExercicio 1')
    v1 = Vector([7.887, 4.138])
    w1 = Vector([-8.802, 6.776])
    print(v1.inner_product(w1))

    print('\tExercicio 2')
    v2 = Vector([-5.955, -4.904, -1.874])
    w2 = Vector([-4.496, -8.755, 7.103])
    print(v2.inner_product(w2))

    print("\n\nANGLE\n\tExercicio 3")
    v3 = Vector([3.183, -7.627])
    w3 = Vector([-2.669, 5.319])
    print(v3.angle_rad(w3))

    print('\tExercicio 4')
    v4 = Vector([7.35, 0.221, 5.188])
    w4 = Vector([2.751, 8.259, 3.985])
    print(v4.angle_degrees(w4))

def dot_product_vector_zero():
    v = Vector([0, 0, 0])
    w = Vector([1, 2, 3])
    print(v.angle_with(w))


def test_scalar():
    v1 = Vector([2,3,4])
    v2 = Vector([2,5,8])
    print(v1.dot(v2))

def test_zip():
    vetor = [ x+y for x, y in zip(range(100), range(100))]
    assert vetor[10] == 20

def test_parallel_or_orthogonal():
    v1 = Vector([-7.579, -7.88])
    w1 = Vector([22.737, 23.64])
    print("Teste 1...\nParalelo\tOrtogonal")
    print(v1.is_parallel_to(w1), v1.is_orthogonal_to(w1))

    v2 = Vector([-2.029, 9.97, 4.172])
    w2 = Vector([-9.231, -6.639, -7.724])
    print("\n\nTeste 2...\nParalelo\tOrthogonal")
    print(v2.is_parallel_to(w2), v2.is_orthogonal_to(w2))

    v3 = Vector([-2.328, -7.284, -1.214])
    w3 = Vector([-1.821, 1.072, -2.94])
    print("\n\nTeste 3...\nParalelo\tOrthogonal")
    print(v3.is_parallel_to(w3), v3.is_orthogonal_to(w3))

    v4 = Vector([2.118, 4.827])
    w4 = Vector([0,0])
    print("\n\nTeste 4...\nParalelo\tOrthogonal")
    print(v4.is_parallel_to(w4), v4.is_orthogonal_to(w4))


#test_magnitude_vetor_unitario()
#test_zip()
#test_scalar()
#dot_product_and_angle()
#dot_product_vector_zero()
#if __name__ == '__main__'
#teste_soma()
test_parallel_or_orthogonal()
