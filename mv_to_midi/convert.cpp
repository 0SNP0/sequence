#include "MidiFile.h"
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;
using namespace smf;

int main(int tpq) {
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
        notes.push_back(a+59);
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