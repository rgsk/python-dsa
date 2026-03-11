.PHONY: cpp

cpp: dist
	g++-15 src/cpp.cpp -Wall -Wno-sign-compare -std=c++20 -o dist/cpp && ./dist/cpp

