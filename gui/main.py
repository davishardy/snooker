""" Snooker App """

from PySide2.QtWidgets import QApplication, QTableWidget, QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel, QCheckBox, QShortcut
from PySide2.QtCore import Qt
from PySide2.QtGui import QKeySequence


import render_utils


class MainWindow(QWidget):
    def __init__(self):
        super().__init__() #inherit qwidget


        # Set up the layout and add the table to it
        layout = QVBoxLayout()

        # Set up the table view widget
        self.table = QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Shot", "Start", "End", "Create Movie", "Render"])

        self.shots = self.load_shots()
        for shot in self.shots:
            self.add_shot(shot, self.table)


        # Create other elements
        # test_label = QLabel("Snooker")
        test_button = QPushButton("Render")
        test_button.clicked.connect(self.render_selected)


        # Add elements to layout
        #layout.addWidget(self.test_label)
        layout.addWidget(self.table)
        layout.addWidget(test_button)

        # Set the layout for the QWidget
        self.setLayout(layout)
        self.setWindowTitle("Snooker")
        self.resize(700, 400)

        # Create a shortcut for 'Ctrl + Q' to close the app
        quit_shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        quit_shortcut.activated.connect(self.close)  # Connect the shortcut to close() method


    def load_shots(self):
        """
        Returns a list of file paths to blender files
        Inputs: None
        Outputs: List of file paths
        """
        shots = render_utils.find_files("i")
        return shots


    def add_shot(self, shot, table_obj):
        """
        Adds a shot to to a table
        Inputs: Shot file path
        Outputs: None, adds shot to table
        """
        # Create Buttons
        row_count = table_obj.rowCount()
        table_obj.insertRow(row_count) # Maybe delete

        shot_label = QLabel(shot.stem)
        shot_label.setAlignment(Qt.AlignCenter)

        start_frame = QLineEdit()
        start_frame.setText(str(1))

        end_frame = QLineEdit()
        end_frame.setText(str(10))

        preview_checkbox = QCheckBox()
        preview_checkbox.setChecked(False)

        render_checkbox = QCheckBox()
        render_checkbox.setChecked(False)

        # Add buttons to rows
        table_obj.setCellWidget(row_count, 0, shot_label) # Shot Label
        table_obj.setCellWidget(row_count, 1, start_frame) # Start Frame
        table_obj.setCellWidget(row_count, 2, end_frame) # End Frame
        table_obj.setCellWidget(row_count, 3, preview_checkbox) # Enable Movie Creation
        table_obj.setCellWidget(row_count, 4, render_checkbox) # Enable Render

    def render_selected(self):
        rows = self.table.rowCount()
        
        for i in range(rows):
            box_widget = self.table.cellWidget(i, 4)
            
            if box_widget.isChecked():
                render_utils.render_file(self.shots[i], 1, 10)
            
        





if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

