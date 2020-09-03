
main: main.o graph.o vertex.o
	g++ -o main -std=c++14 main.o graph.o vertex.o

main.o: main.cpp 
	g++ -c -std=c++14 main.cpp -I.

graph.o: graph.cpp
	g++ -c -std=c++14 graph.cpp -I.

vertex.o: vertex.cpp
	g++ -c -std=c++14 vertex.cpp -I.	
clean:
	rm main
	rm *o
