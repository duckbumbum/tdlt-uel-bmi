from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QInputDialog, QMessageBox

from MainWindow import Ui_MainWindow


class CustomerManagementApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Kết nối các nút với sự kiện
        self.ui.btnAdd.clicked.connect(self.add_customer)
        self.ui.btnEdit.clicked.connect(self.edit_customer)
        self.ui.btnDelete.clicked.connect(self.delete_customer)
        self.ui.btnView.clicked.connect(self.view_customer)

    def add_customer(self):
        row_position = self.ui.tblCustomers.rowCount()
        self.ui.tblCustomers.insertRow(row_position)
        self.ui.tblCustomers.setItem(row_position, 0, QTableWidgetItem(str(row_position + 1)))
        self.ui.tblCustomers.setItem(row_position, 1, QTableWidgetItem("Nguyễn Văn A"))
        self.ui.tblCustomers.setItem(row_position, 2, QTableWidgetItem("0123456789"))
        self.ui.tblCustomers.setItem(row_position, 3, QTableWidgetItem("Hà Nội"))

    def edit_customer(self):
        # Lấy chỉ mục của hàng được chọn
        selected_row = self.ui.tblCustomers.currentRow()
        if selected_row < 0:  # Nếu không có khách hàng nào được chọn
            QMessageBox.warning(self, "Chỉnh sửa thất bại", "Vui lòng chọn một khách hàng để chỉnh sửa.")
            return

        # Lấy thông tin cũ của khách hàng
        name = self.ui.tblCustomers.item(selected_row, 1).text()
        phone = self.ui.tblCustomers.item(selected_row, 2).text()
        address = self.ui.tblCustomers.item(selected_row, 3).text()

        # Mở hộp thoại nhập thông tin mới
        new_name, ok1 = QInputDialog.getText(self, "Chỉnh sửa tên", "Nhập tên khách hàng:", text=name)
        if not ok1:
            return
        new_phone, ok2 = QInputDialog.getText(self, "Chỉnh sửa số điện thoại", "Nhập số điện thoại:", text=phone)
        if not ok2:
            return
        new_address, ok3 = QInputDialog.getText(self, "Chỉnh sửa địa chỉ", "Nhập địa chỉ:", text=address)
        if not ok3:
            return

        # Cập nhật thông tin vào bảng
        self.ui.tblCustomers.setItem(selected_row, 1, QTableWidgetItem(new_name))
        self.ui.tblCustomers.setItem(selected_row, 2, QTableWidgetItem(new_phone))
        self.ui.tblCustomers.setItem(selected_row, 3, QTableWidgetItem(new_address))

    def delete_customer(self):
        # Lấy chỉ mục của hàng được chọn
        selected_row = self.ui.tblCustomers.currentRow()
        if selected_row < 0:  # Nếu không có khách hàng nào được chọn
            QMessageBox.warning(self, "Xóa thất bại", "Vui lòng chọn một khách hàng để xóa.")
            return

        # Xác nhận trước khi xóa
        reply = QMessageBox.question(self, 'Xác nhận', 'Bạn có chắc chắn muốn xóa khách hàng này?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.ui.tblCustomers.removeRow(selected_row)

    def view_customer(self):
        # Lấy chỉ mục của hàng được chọn
        selected_row = self.ui.tblCustomers.currentRow()
        if selected_row < 0:  # Nếu không có khách hàng nào được chọn
            QMessageBox.warning(self, "Xem thất bại", "Vui lòng chọn một khách hàng để xem chi tiết.")
            return

        # Lấy thông tin của khách hàng
        name = self.ui.tblCustomers.item(selected_row, 1).text()
        phone = self.ui.tblCustomers.item(selected_row, 2).text()
        address = self.ui.tblCustomers.item(selected_row, 3).text()

        # Hiển thị thông tin chi tiết
        details = f"Thông tin khách hàng:\n\nTên: {name}\nSố điện thoại: {phone}\nĐịa chỉ: {address}"
        QMessageBox.information(self, "Chi tiết khách hàng", details)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = CustomerManagementApp()
    window.show()
    sys.exit(app.exec())
