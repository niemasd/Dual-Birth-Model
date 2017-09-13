# use g++ compiler with C++11 support
CXX=g++
CXXFLAGS=-Wall -pedantic -O3
TOOLS=dualbirth

# compile all tools
all: $(TOOLS)

# dualbirth: Simulate trees under the Dual-Birth model in O(n)
numlist: dualbirth.cpp
	$(CXX) $(CXXFLAGS) -o dualbirth dualbirth.cpp

# remove all compiled files
clean:
	$(RM) $(TOOLS) *.o
