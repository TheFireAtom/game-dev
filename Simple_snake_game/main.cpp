#include <iostream>
#include <ncurses.h>
#include <vector>
#include <deque>

std::vector<char> map;
int mapLength = 20;
int mapWidth = 15;

struct snakePart {
	int x;
	int y;
};

enum class Dir { UP, DOWN, LEFT, RIGHT };

struct Game {
	int score = 0;
	bool running = false;
};

void createMap() {
	for (int y = 0; y < mapWidth; y++) {
		for (int x = 0; x < mapLength; x++) {
			if (y == 0 || y == mapWidth-1 || x == 0 || x == mapLength-1) {
				mvaddch(y, x, '#');
			} else {
				mvaddch(y, x, '.');
			}
		}
	std::cout << '\n';
	}
}

int main() {
	initscr();
	cbreak(); // line buffering disable
	noecho(); // no character from user input
	keypad(stdscr, TRUE); 

	createMap();
	//refresh();

	getch();

	endwin(); // clean up ncurses
	
	return 0;
}