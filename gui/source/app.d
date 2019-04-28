import dlangui;
import std.process: executeShell;

mixin APP_ENTRY_POINT;

Widget gLayout;

extern (C) int UIAppMain(string[] args) {
    // create window
    Window window = Platform.instance.createWindow("GKL_DEBUG", null);

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
        }


        DirEditLine {
            id: dirNameEdit
            text: "Save folder..."
        }
        EditLine {
            id: fileNameEdit
        }
    }

	Button {
        id: saveClock
        text: "Create"
    }
}

		}
	);

	gLayout = layout;
	window.mainWidget = gLayout;

    ( cast( ComboBox )( layout.childById( "modelCombo" ) ) ).items = [ "Natural minor" ];
	( cast( ComboBox )( layout.childById( "tonCombo" ) ) ).items = [ "test1", "test2" ];

    auto clickHandler = new COnClickHandler();
    layout.childById("saveClock").click = clickHandler;

    // show window
    window.show();

    // run message loop
    return Platform.instance.enterMessageLoop();
}

class COnClickHandler : OnClickHandler {
    bool onClick( Widget src ) {
        //string temp = (cast( EditLine )gLayout.childById( "tempCombo" ) ).text;
        //string ton = (cast( EditLine )gLayout.childById( "tonCombo" ) ).text;
        //string lenght = (cast( EditLine )gLayout.childById( "lenghtCombo" ) ).text;

        Log.i("Execute gen.py");
        auto genExec = executeShell("python ../melody_generator/gen.py 120 2 8");
        if (genExec.status != 0) {
            Log.i(genExec.output);
            return false;
        }
        return true;
    }
}