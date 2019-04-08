#include "MidiFile.h"
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;
using namespace smf;

int to_note(int keynote, int ton, string harmony = "natural_minor") {
    if (harmony == "natural_minor") {
        --keynote;
        int oct = keynote / 7;
        keynote = keynote % 7;
        switch (keynote)
        {
            case 0:
                keynote = 60 + oct * 12;
                break;
            case 1:
                keynote = 62 + oct * 12;
                break;
            case 2:
                keynote = 63 + oct * 12;
                break;
            case 3:
                keynote = 65 + oct * 12;
                break;
            case 4:
                keynote = 67 + oct * 12;
                break;
            case 5:
                keynote = 68 + oct * 12;
                break;
            case 6:
                keynote = 70 + oct * 12;
                break;
            default:
                break;
        }
    }
    return keynote + ton;
}

int main(int tpq) {
    int ton = 2;
    cout << ton << endl;
    MidiFile fout;
    fout.absoluteTicks();
    fout.addTrack(1);
    vector<uchar> midievent;
    midievent.resize(3);
    fout.setTicksPerQuarterNote(tpq);
    string mv_path="../melody.seq";
    ifstream fin(mv_path);
    vector<int> notes;
    vector<double> rhytm;
    double a;
    while (fin >> a) {
        notes.push_back(to_note(a, ton)); 
        fin >> a;
        rhytm.push_back(a*4);
    }
    notes.push_back(-1);
    rhytm.push_back(-1);
    for (auto &e: notes) {
        cout << e << ' ';
    }
    cout << endl;
    for (auto &e: rhytm) {
        cout << e << ' ';
    }
    double actiontime = 0;
    midievent[2] = 64;
    for (int i = 0; notes[i] >=0; ++i) {
        midievent[0] = 0x90;
        midievent[1] = notes[i];
        fout.addEvent(1, actiontime, midievent);
        actiontime += tpq*rhytm[i];
        midievent[0] = 0x80;
        fout.addEvent(1, actiontime, midievent);
    }
    fout.sortTracks();
    fout.write("melody.mid");
    return 0;
}