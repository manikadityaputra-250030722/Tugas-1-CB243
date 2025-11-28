"""Studi Kasus 1 - Definisi Model

Kelas yang diimplementasikan :
- Address
- Person (dasar)
- Student (turunan Person)
- Professor (turunan Person) """
from __future__ import annotations
from typing import Optional, List


class Address:
    """Representasi alamat tempat tinggal

    Attribut:
        street (str) : Nama jalan
        city (str) : Kota
        state (str) : Provinsi
        postal_code (int) : Kode pos
        country (str) = Negara """

    def __init__(self, street: str, city: str, state: str, postal_code: int, country: str):
        """Menginisiasi objek Adress"""
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country

    def validate(self) -> bool:
        """Memvalidasi data alamat
        Returns True jika semua string fields tidak kosong dan postal_code itu isinya integer"""
        if not all(isinstance(x, str) and x.strip() for x in (self.street, self.city, self.state, self.country)):
            return False
        if not isinstance(self.postal_code, int) or self.postal_code <= 0:
            return False
        return True

    def output_as_label(self) -> str:
        """Mengembalikan alamat dalam format satu baris"""
        return f"{self.street}, {self.city}, {self.state} {self.postal_code}, {self.country}"


class Person:
    """Kelas Dasar untuk entitas orang atau manusia

    Attribut:
        name (str) : Nama lengkap
        phone_number (str) : Nomor telepon
        email_address (str) : Alamat email.
        address (Optional[Address]) : Alamat tempat tinggal """

    def __init__(self, name: str, phone_number: str, email_address: str, address: Optional[Address] = None):
        """Menginisialisasi objek Person"""
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address
        self.address = address

    def purchase_parking_pass(self) -> str:
        """Simulasi pembelian kartu parkir"""
        return f"Parking pass purchased for {self.name}"


class Student(Person):
    """Kelas student yang merupakan turunan dari person.

    Attribut:
        student_number (int) : Nomor mahasiswa
        average_mark (int) : Nilai rata-rata
        supervisors (List[Professor]) : Daftar profesor atau dosen pembimbing"""

    def __init__(self, name: str, phone_number: str, email_address: str, student_number: int, average_mark: int, address: Optional[Address] = None):
        super().__init__(name, phone_number, email_address, address)
        self.student_number = student_number
        self.average_mark = average_mark
        self.supervisors: List[Professor] = []

    def is_eligible_to_enroll(self, program: str) -> bool:
        """Mengecek apakah mahasiswa memenuhi syarat mendaftar bimbingan (menggunakan nilai rata-rata: 60)."""
        return self.average_mark >= 60

    def get_seminars_taken(self) -> int:
        """Mengembalikan jumlah seminar yang pernah diambil (nilai rata-rata dibagi 10)"""
        return max(0, self.average_mark // 10)

    def add_supervisor(self, professor: 'Professor') -> None:
        """Menambakan profesor ebagai pembimbing mahasiswa"""
        if professor not in self.supervisors:
            self.supervisors.append(professor)


class Professor(Person):
    """Kelas professor yang merupakan turunan dari person.

    Attribut:
        salary (int) : Gaji
        _staff_number (int) : nomor staff (protected)
        __years_of_service (int) : lama bekerja (private)
        number_of_classes (int) : jumlah kelas yang diajar
        supervisees (List[Student]) : daftar mahasiswa yang dibimbing"""

    def __init__(self, name: str, phone_number: str, email_address: str, salary: int, staff_number: int, years_of_service: int, number_of_classes: int, address: Optional[Address] = None):
        super().__init__(name, phone_number, email_address, address)
        self.salary = salary
        self._staff_number = staff_number
        self.__years_of_service = years_of_service
        self.number_of_classes = number_of_classes
        self.supervisees: List[Student] = []

    def add_supervisee(self, student: Student) -> bool:
        """Menambahkan mahasiswa sebagai supervise

        Aturan : maksimal 5 supervise"""
        if student in self.supervisees:
            return False
        if len(self.supervisees) >= 5:
            return False
        self.supervisees.append(student)
        student.add_supervisor(self)
        return True

    def get_years_of_service(self) -> int:
        """Mengembalikan lama masa kerja profesor (private attribut)."""
        return self.__years_of_service