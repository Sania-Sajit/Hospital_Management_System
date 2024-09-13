class Doctor:
    def __init__(self,doc_id,name,dept,contact_no):
        self.doc_id = doc_id
        self.doc_name = name
        self.department = dept
        self.contact = contact_no

    def __str__(self):
        return f"ID: {self.doc_id} \nName: {self.doc_name}\nDepartment: {self.department}\nContact No.: {self.contact}\n"

class Appointment:
    def __init__(self,app_id,patient,doc,date,time):
        self.appointment_id = app_id
        self.patient = patient
        self.doctor = doc
        self.date = date
        self.time = time
    
    def __str__(self):
        return f"Appointment ID: {self.appointment_id}\nPatient: {self.patient}\nDoctor: {self.doctor}\nDate: {self.date}\nTime: {self.time}\n"

class MedicalRecord:
    def __init__(self, date, diagnosis, treatment, prescription):
        self.date = date
        self.diagnosis = diagnosis
        self.treatment = treatment
        self.prescription = prescription
    def __str__(self):
        return f"Date: {self.date}\nDiagnosis: {self.diagnosis}\nTreatment provided: {self.treatment}\nPrescription: {self.prescription}\n"


class Patient:
    def __init__(self,p_id,name,age,gender,contact):
        self.patient_id = p_id
        self.patient_name = name
        self.age = age
        self.gender = gender
        self.contact_no = contact
        self.med_records = []

    def add_med_record(self,record):
        self.med_records.append(record)
    
    def view_med_record(self):
        print("Past medical records: \n")
        for record in self.med_records:
            print(f"Date: {record.date}\nDiagnosis: {record.diagnosis}\nTreatment provided: {record.treatment}\nPrescription: {record.prescription}")
    
    def __str__(self):
        return f"ID: {self.patient_id}\nName: {self.patient_name}\nAge: {self.age}\nGender: {self.gender}\nContact No.: {self.contact_no}\n "

class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self,patient):
        for pat in self.patients:
            if pat.patient_id == patient.patient_id:
                print("Patient already exists...\n")
                break
        else:
            self.patients.append(patient)
    
    def view_all_patients(self):
        for patient in self.patients:
            print(patient)

    def search_patient(self,req_patient_ID):
        for patient in self.patients:
            if str(patient.patient_id) == req_patient_ID:
                print(patient)
                break
        else:
            print(f"Patient with ID '{req_patient_ID}' does not exist")
        
    def update_patient_info(self,pat_ID,name=None,age=None,gender=None,contact=None):
        req_patient = False
        for patient in self.patients:
            if str(patient.patient_id) == pat_ID:
                req_patient = patient
                break
        if req_patient == False:
            print("Patient not found")
        else:
            if name:
                req_patient.patient_name = name
            if age:
                req_patient.age = int(age)
            if gender:
                req_patient.gender = gender
            if contact:
                req_patient.contact_no = contact
            print("Patient info updated successfully\n")

    def add_doc(self,doc):
        for d in self.doctors:
            if d.doc_id == doc.doc_id:
                print("Doctor already exists...\n")
                break
        else:
            self.doctors.append(doc)
    
    def view_doc(self):
        for doc in self.doctors:
            print(doc)

    def search_doc(self,req_doc_ID):
        for doc in self.doctors:
            if str(doc.doc_id) == req_doc_ID:
                print(doc)
                break   
        else:
            print(f"Doctor with ID '{req_doc_ID}' does not exist")
        

    def schedule_appointment(self,appointment):
        self.appointments.append(appointment)

    def view_appointments(self):
        for app in self.appointments:
            print(app)


def main():
    hospital = Hospital()
    
    while True:
        print("1. Add new patient\n2. View all patients\n3. Search for a patient\n4. Update patient information\n5. Add medical record of a patient\n6. View medical records of a patient")
        print("7. Add new doctor\n8. View all doctors\n9. Search for a doctor\n10. Schedule an appointment\n11. View all appointments\n12. Exit")
        
        choice = int(input("Enter a choice (1-12): "))
        
        if choice == 1:
            p_id = input("Enter patient ID: ")
            name = input("Enter patient name: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender: ")
            contact = input("Enter contact number: ")
            patient = Patient(p_id, name, age, gender, contact)
            hospital.add_patient(patient)
            print("Patient added successfully.")
        
        elif choice == 2:
            hospital.view_all_patients()
        
        elif choice == 3:
            req_patient_ID = input("Enter patient ID to be searched: ")
            hospital.search_patient(req_patient_ID)
        
        elif choice == 4:
            pat_ID = input("Enter patient ID to be updated: ")
            req_patient = False
            for patient in hospital.patients:
                if str(patient.patient_id) == pat_ID:
                    req_patient = patient
                    break
            if req_patient == False:
                print("Patient not found")
            else:
                name = input("Enter new name (or press Enter to skip): ")
                age = input("Enter new age (or press Enter to skip): ")
                gender = input("Enter new gender (or press Enter to skip): ")
                contact = input("Enter new contact number (or press Enter to skip): ")

                if name:
                    name=name
                else:
                    name=None

                if gender:
                    gender=gender
                else:
                    gender=None

                if age:
                    age=int(age)
                else:
                    age=None

                if contact:
                    contact=contact
                else:
                    contact=None

                hospital.update_patient_info(pat_ID, name , int(age), gender, contact)
        
        elif choice == 5:
            p_id = input("Enter patient ID to add record: ")
            patient = None
            for pat in hospital.patients:
                if pat.patient_id == p_id:
                    patient = pat
                    break
            if patient == None:
                print("Patient not found!")
                continue

            date = input("Enter record date (YYYY-MM-DD): ")
            diagnosis = input("Enter diagnosis: ")
            treatment = input("Enter treatment provided: ")
            prescription = input("Enter prescription: ")
            record = MedicalRecord(date, diagnosis, treatment, prescription)
            patient.add_med_record(record)
            print("Medical record added successfully.")
        
        elif choice == 6:
            p_id = input("Enter patient ID to view records: ")
            patient = None
            for pat in hospital.patients:
                if pat.patient_id == p_id:
                    patient = pat
                    break
            if patient == None:
                print("Patient not found!")
                continue

            patient.view_med_record()
        
        elif choice == 7:
            doc_id = input("Enter doctor ID: ")
            name = input("Enter doctor name: ")
            dept = input("Enter department: ")
            contact = input("Enter contact number: ")
            doctor = Doctor(doc_id, name, dept, contact)
            hospital.add_doc(doctor)
            print("Doctor added successfully.")
        
        elif choice == 8:
            hospital.view_doc()
        
        elif choice == 9:
            req_doc_ID = input("Enter doctor ID to search: ")
            hospital.search_doc(req_doc_ID)
        
        elif choice == 10:
            app_id = input("Enter appointment ID: ")
            p_id = input("Enter patient ID: ")
            patient = None
            for pat in hospital.patients:
                if pat.patient_id == p_id:
                    patient = pat
                    break
            if patient == None:
                print("Patient not found!")
                continue

            doc_id = input("Enter doctor ID: ")
            doctor = None
            for doc in hospital.doctors:
                if doc.doc_id == doc_id:
                    doctor = doc
                    break
            if doctor == None:
                print("Doctor not found!")
                continue

            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time (HH:MM): ")
            appointment = Appointment(app_id, patient, doctor, date, time)
            hospital.schedule_appointment(appointment)
            print("Appointment scheduled successfully.")

        elif choice == 11:
            hospital.view_appointments()
        
        elif choice == 12:
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()            

