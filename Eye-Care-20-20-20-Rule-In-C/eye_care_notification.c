#include <windows.h>

void display_notification() {
    MessageBox(NULL,"Take a 20-second break!\nLook at something 20 feet away.", "20-20-20 Rule", MB_OK | MB_ICONINFORMATION);
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) {
    while (1) {
        Sleep(1000*60*20); // Sleep for 20 minutes
        display_notification();
    }
    return 0;
    
    //compile it with "gcc -o eye_care_notification.exe eye_care_notification.c -mwindows"
    //keep the resultant .exe file shortcut in to the start up folder (win+R and type "shell:startup")
}