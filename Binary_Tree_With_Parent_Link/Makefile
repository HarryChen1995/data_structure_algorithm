main: main.o tree.o node.o
	g++ -o main main.o tree.o node.o

main.o: main.cpp tree.cpp node.cpp
	g++ -fpic -c main.cpp tree.cpp -I./tree node.cpp -I./node

node.o: node.cpp
	g++ -fpic -c node.cpp -I./node

tree.o: tree.cpp
	g++ -fpic -c tree.cpp -I./tree -I./node

clean:
	rm *.o
	rm main
