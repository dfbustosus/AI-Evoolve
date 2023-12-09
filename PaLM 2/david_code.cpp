#include <iostream>
#include <array>
#include <stdexcept>

template<typename T, size_t N>
class Vector {
private:
    std::array<T, N> elements;

public:
    Vector(std::initializer_list<T> values) {
        if (values.size() != N) {
            throw std::length_error("Numero incorrecto de elementos en la lista a inicializar");
        }
        size_t i = 0;
        for (const T& val : values) {
            elements[i++] = val;
        }
    }

    T& operator[](size_t index) {
        if (index >= N) {
            throw std::out_of_range("Index fuera de rango");
        }
        return elements[index];
    }

    const T& operator[](size_t index) const {
        if (index >= N) {
            throw std::out_of_range("Index fuera de rango");
        }
        return elements[index];
    }

    void print() const {
        std::cout << "[";
        for (size_t i = 0; i < N; ++i) {
            std::cout << elements[i];
            if (i != N - 1) {
                std::cout << ", ";
            }
        }
        std::cout << "]" << std::endl;
    }
};

template<typename T, size_t N>
class ThreeDimensionalVector : public Vector<T, N> {
public:
    ThreeDimensionalVector(T x, T y, T z) : Vector<T, N>({x, y, z}) {}
};

int main() {
    try {
        Vector<double, 4> vec1 = {1.2, 3.4, 5.6, 7.8};
        vec1.print();

        ThreeDimensionalVector<int, 3> vec2(3, 4, 5);
        vec2.print();

        // Access out-of-range element
        std::cout << "Accediendo a vec1[5]: ";
        std::cout << vec1[5] << std::endl;
    } catch (const std::exception& e) {
        std::cout << "Exception occurrio en: " << e.what() << std::endl;
    }

    return 0;
}
