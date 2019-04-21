import dlangui;

mixin APP_ENTRY_POINT;

extern (C) int UIAppMain(string[] args) {
    // create window
    Window window = Platform.instance.createWindow("GKL_DEBUG", null, WindowFlag.Modal, 500, 210);

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
        ComboBox {
            id: tempCombo
        }


        TextWidget {
            id: toneText
            text: "Tone"
        }
        ComboBox {
            id: toneCombo
        }


        TextWidget {
            id: tickText
            text: "Tick"
        }
        ComboBox {
            id: tickCombo
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
        text: "Compile"
    }
}

		}
	);

	window.mainWidget = layout;

	( cast( ComboBox )( layout.childById( "tempCombo" ) ) ).items = [ "test1", "test2" ];
	( cast( ComboBox )( layout.childById( "toneCombo" ) ) ).items = [ "test1", "test2" ];
	( cast( ComboBox )( layout.childById( "tickCombo" ) ) ).items = [ "test1", "test2" ];

    // show window
    window.show();

    // run message loop
    return Platform.instance.enterMessageLoop();
}
