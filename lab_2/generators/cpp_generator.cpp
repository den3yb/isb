#include <iostream>
#include <random>

void generate_seq(bool* p, const int size){
    for(int i = 0; i < size ; i++ ){
        p[i] = std::rand() % 2;
    }
}

int main(){
    int const size = 128;
    bool sequence[size];
    generate_seq(sequence, size);
    for (int i = 0; i < size; i++) {
        std::cout << sequence[i];
    }   
    return 0;
}