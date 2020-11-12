# distutils: language=c++

from libcpp.vector cimport vector

def primes(unsigned int nb_primes):
    cdef int n, i
    cdef vector[int] p
    # allocate memory for 'nb_primes' elements.
    p.reserve(nb_primes)  

    n = 2
    # size() for vectors is similar to len()
    while p.size() < nb_primes:  
        for i in p:
            if n % i == 0:
                break
        else:
            # push_back is similar to append()
            p.push_back(n)  
        n += 1

    # Vectors are automatically converted to Python
    # lists when converted to Python objects.
    return p
