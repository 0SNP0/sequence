import dlangui;
import dlangui.dialogs.filedlg;
import std.string : replace;
import std.process;

mixin APP_ENTRY_POINT;

//enum PROCESS_FILE = "gen.py";
//enum EXECUTE_COMMAND_GEN = ".\\penv\\python.exe " ~ PROCESS_FILE ~ " (%#1) (%#2) (%#3) (%#4)";

Widget gLayout;

extern (C) int UIAppMain(string[] args) {
    // create window
    Window window = Platform.instance.createWindow("Sequence", null);

	auto layout = parseML( q{
VerticalLayout {
    id: vlayout
    margins: Rect { left: 5; right: 3; top: 2; bottom: 4 }
    padding: Rect { 5, 4, 3, 2 } // same as Rect { left: 5; top: 4; right: 3; bottom: 2 }
    TableLayout {
        colCount: 2

        TextWidget {
            id: tempText
            text: "Temp"
        }
        EditLine {
            id: tempCombo
            text: "120"
        }


        TextWidget {
            id: nnText
            text: "Model"
        }
        ComboBox {
            id: modelCombo
        }


        TextWidget {
            id: tonText
            text: "Tonality"
        }
        ComboBox {
            id: tonCombo
        }


        TextWidget {
            id: lenghtText
            text: "Lenght"
        }
        EditLine {
            id: lenghtCombo
            text: "8"
        }


        DirEditLine {
            id: dirNameEdit
            text: ""
        }
        EditLine {
            id: fileNameEdit
            text: "melody.mid"
        }
    }

	Button {
        id: saveClock
        text: "Create"
    }

    Button {
        id: trainButton
        text: "Train"
    }
}

		}
	);

	gLayout = layout;
	window.mainWidget = gLayout;

    ( cast( ComboBox )( layout.childById( "modelCombo" ) ) ).items = [ "Natural minor"d ];
	( cast( ComboBox )( layout.childById( "tonCombo" ) ) ).items = [ "C"d, "C#;"d, "D"d, "D#"d, "E"d, "F"d, "F#"d, "G"d, "G#"d, "A"d, "B"d, "H"d ];

    auto clickHandler = new COnClickHandler();
    layout.childById("saveClock").click = clickHandler;
    auto tClickHandler = new TOnClickHandler;
    layout.childById("trainButton").click = tClickHandler;

    // show window
    window.show();

    // run message loop
    return Platform.instance.enterMessageLoop();
}

class COnClickHandler : OnClickHandler {
    bool onClick( Widget src ) {
        /*const string resExecCommand =
            EXECUTE_COMMAND_GEN .replace("(%#1)", (cast(EditLine)gLayout.childById("tempCombo")).text)
                        .replace("(%#2)", to!string((cast(ComboBox)gLayout.childById("tonCombo")).selectedItemIndex))
                        .replace("(%#3)", (cast(EditLine)gLayout.childById("lenghtCombo")).text)
                        .replace( "(%#4)", 
                            ( cast( DirEditLine )gLayout.childById( "dirNameEdit" ) ).text ~  
                            ( cast( EditLine )gLayout.childById( "fileNameEdit" ) ).text );
        
        Log.i( "Execute: " ~ resExecCommand );
        auto genExec = executeShell( resExecCommand );
        if (genExec.status != 0) {
            Log.i(genExec.output);
            return false;
        }
        return true;
        */
        auto genExec = spawnProcess(["penv\\python.exe", "gen.py", to!string((cast(EditLine)gLayout.childById("tempCombo")).text), to!string((cast(ComboBox)gLayout.childById("tonCombo")).selectedItemIndex), to!string((cast(EditLine)gLayout.childById("lenghtCombo")).text), to!string((cast(DirEditLine)gLayout.childById("dirNameEdit")).text~(cast(EditLine)gLayout.childById("fileNameEdit") ).text)]);
        return true;
    }
}

class TOnClickHandler : OnClickHandler {
    bool onClick( Widget src ) {
        auto trainExec = spawnProcess(["penv\\python.exe", "train.py"]);
        return true;
    }
}