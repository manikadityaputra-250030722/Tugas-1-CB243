#Entry point untuk Studi Kasus 1
from models import Address, Student, Professor

def main():
    # membuat sebuah objek alamat dan memvalidasinya
    addr = Address('123 Campus Rd', 'Bandung', 'Jawa Barat', 40132, 'Indonesia')
    print('Alamat:', addr.output_as_label())
    print('Alamat Valid?', addr.validate())

    # Create sebuah objek professor dan student
    prof = Professor('Dr. Yohan', '08123456789', 'yohanz@univ.ac.id', salary=8000, staff_number=42, years_of_service=10, number_of_classes=3, address=addr)
    stud = Student('Jano', '08987654321', 'jano@student.univ.ac.id', student_number=2023001, average_mark=75)

    # Menjalankan berbagai fungsi
    print(prof.purchase_parking_pass())
    added = prof.add_supervisee(stud)
    print('Supervisee ditambahkan:', added)
    print('Jumlah supervisee profesor:', len(prof.supervisees))
    print('Jumlah supervisor mahasiswa:', len(stud.supervisors))
    print('Mahasiswa memenuhi syarat daftar?', stud.is_eligible_to_enroll('Computer Science'))
    print('Perkiraan seminar yang pernah diambil:', stud.get_seminars_taken())

if __name__ == '__main__':
    main()