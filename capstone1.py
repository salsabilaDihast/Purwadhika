dataKaryawan = [ 
    {
        'id_karyawan' : 5001,
        'nama': 'GIVON',
        'gender': 'L',
        'no_hp': '08988975142',
        'divisi': 'Marketing'
    },
    {
        'id_karyawan' : 4001,
        'nama': 'DHIRA',
        'gender': 'P',
        'no_hp': '081321743559',
        'divisi': 'IT'
    },
    {
        'id_karyawan' : 2001,
        'nama': 'LAMIRA',
        'gender': 'P',
        'no_hp': '08982563744',
        'divisi': 'FINANCE'
    },
    {
        'id_karyawan' : 3001,
        'nama': 'YUSUF',
        'gender': 'L',
        'no_hp': '081842993572',
        'divisi': 'HRD'
    },
    {
        'id_karyawan' : 1001,
        'nama': 'VEGA',
        'gender': 'P',
        'no_hp': '081642375198',
        'divisi': 'CREATIVE'
    }
]

def data_Seluruh() :
    print('\n\t\t\t\tData Seluruh Karyawan \n-------------------------------------------------------------------------------------')
    print('  INDEX  |  ID KARYAWAN   |\tNAMA\t  | GENDER |\t  NOMOR HP\t|   DIVISI')
    print('-------------------------------------------------------------------------------------')
    for i in range(len(dataKaryawan)):
        print('    {}\t |     {}\t  |\t{}\t  |   {}\t   |     {}\t|  {}'.format(i, dataKaryawan[i]['id_karyawan'], dataKaryawan[i]['nama'], dataKaryawan[i]['gender'], dataKaryawan[i]['no_hp'], dataKaryawan[i]['divisi']))

def baca_Data():
    while True :
        bacaData = input('''\n
        ---------------Menampilkan Data Karyawan---------------
        
        Pilihan Menu :

        1. Data Seluruh Karyawan
        2. Data Karyawan Tertentu
        3. Kembali ke Menu Utama

        Masukkan angka sub menu yang ingin dijalankan : ''')
        if (bacaData == '1') :
            if (len(dataKaryawan) <= 0):
                    print('\t=======================================================')
                    print('\t\t\t    Tidak Ada Data')
                    print('\t=======================================================')
            else :
                data_Seluruh()
        elif (bacaData == '2') :
            if (len(dataKaryawan) <= 0): 
                print('\t=======================================================')
                print('\t\t\t    Tidak Ada Data')
                print('\t=======================================================')
            else:
                inputBaca = int(input('\n\nMasukkan index data karyawan yang ingin ditampilkan: '))
                if (inputBaca < len(dataKaryawan)):
                    print('\nData karyawan dengan index {}'.format(inputBaca))
                    print('-------------------------------------------------------------------------------------\n  INDEX   |  ID KARYAWAN  |\tNAMA\t  | GENDER |\t  NOMOR HP\t|   DIVISI')
                    print('-------------------------------------------------------------------------------------')
                    print('    {}\t  |     {}\t  |\t{}\t  |   {}\t   |     {}\t|  {}'.format(inputBaca, dataKaryawan[inputBaca]['id_karyawan'], dataKaryawan[inputBaca]['nama'], dataKaryawan[inputBaca]['gender'], dataKaryawan[inputBaca]['no_hp'], dataKaryawan[inputBaca]['divisi']))
                else: 
                    print('\nData karyawan dengan index {}'.format(inputBaca))
                    print('===============================================================')
                    print('\t\t\tTidak Ada Data')
                    print('===============================================================')              
        elif (bacaData == '3') :
            break
                          
def tambah_Data() :
    while True :
        tambahData = input('''\n
        ---------------Menambah Data Karyawan---------------
       
        Pilihan Menu :

        1. Tambah Data Karyawan
        2. Kembali ke Menu Utama

        Masukkan angka sub menu yang ingin dijalankan : ''')
        if (tambahData == '1') :
            inputTambah = int(input('\nMasukkan index data karyawan: '))
            if (inputTambah < len(dataKaryawan)):
                print('============================================================')
                print('\t\t      Data Sudah Ada')
                print('============================================================')
            elif (inputTambah == len(dataKaryawan)):
                id_Karyawan = int(input('\nMasukkan ID Karyawan : '))
                namaKaryawan = input('Masukkan Nama Karyawan : ').upper()
                genderKaryawan = input('Masukkan Gender Karyawan (P/L) : ').upper()
                no_HPKaryawan = input('Masukkan No. HP Karyawan : ')
                divisiKaryawan = input('Masukkan Divisi Karyawan : ').upper()
                while True:
                    choice = input('\nApakah Anda yakin data ingin ditambahkan?(Y/N) : ').upper()
                    if (choice == 'Y') :
                        dataKaryawan.append({
                        'id_karyawan' : id_Karyawan,
                        'nama' : namaKaryawan,
                        'gender' : genderKaryawan,
                        'no_hp' : no_HPKaryawan,
                        'divisi' : divisiKaryawan
                    })
                        print('============================================================')
                        print('\t\t      Data Tersimpan')
                        print('============================================================')
                        break
                    elif (choice == 'N') : 
                        break
        elif (tambahData == '2') :
            break

def perbarui_Data() :
    while True :
        perbaruiData = input('''\n
        ---------------Memperbarui Data Karyawan---------------
         
        Pilihan Menu :
         
        1. Perbarui Data Karyawan
        2. Kembali ke Menu Utama
        
        Masukkan angka sub menu yang ingin dijalankan : ''')
        if (perbaruiData == '1') :
            inputPerbarui = int(input('\nMasukkan index data karyawan yang ingin diperbarui: '))
            if (inputPerbarui < len(dataKaryawan)):
                print('\n-------------------------------------------------------------------------------------\n  INDEX   |  ID KARYAWAN  |\tNAMA\t  | GENDER |\t  NOMOR HP\t|   DIVISI')
                print('-------------------------------------------------------------------------------------')
                print('    {}\t  |     {}\t  |\t{}\t  |   {}\t   |     {}\t|  {}'.format(inputPerbarui, dataKaryawan[inputPerbarui]['id_karyawan'], dataKaryawan[inputPerbarui]['nama'], dataKaryawan[inputPerbarui]['gender'], dataKaryawan[inputPerbarui]['no_hp'], dataKaryawan[inputPerbarui]['divisi']))
                while True:
                    choice = input('\nApakah Anda ingin lanjut memperbarui data?(Y/N) : ').upper()
                    if (choice == 'N') :
                        print('===============================================================')
                        print('\t\t     Data Tidak Terupdate')
                        print('===============================================================')
                        break
                    elif (choice == 'Y') :
                        kolom = input('\nMasukkan kolom yang ingin diperbarui : ')
                        namaBaru = input('Masukkan nama baru : ').upper()
                        
                        while True:
                            choice = input('\nApakah Anda yakin data ingin diperbarui?(Y/N) : ').upper()
                            if (choice == 'Y') :
                                if (kolom == 'nama' ) :
                                    dataKaryawan[inputPerbarui]['nama'] = namaBaru
                                    print('============================================================')
                                    print('\t\t      Data Updated')
                                    print('============================================================')
                                    break
                            elif (choice == 'N') :
                                print('===============================================================')
                                print('\t\t     Data Tidak Terupdate')
                                print('===============================================================')
                                break
                        break
            else: 
                print('===============================================================')
                print('\t\t\tTidak Ada Data')
                print('===============================================================')
        elif (perbaruiData == '2') :
            break

def hapus_Data() : 
    while True:
        hapusData = input('''\n
        ---------------Menghapus Data Karyawan---------------

        Pilihan Menu :

        1. Hapus Data Karyawan
        2. Kembali ke Menu Utama
            
        Masukkan angka sub menu yang ingin dijalankan : ''')
        if (hapusData == '1') :
            inputHapus = int(input('\nMasukkan index data karyawan yang ingin dihapus : '))
            if (inputHapus >= len(dataKaryawan)):
                print('=============================================================')
                print('\t       Data yang Anda Cari Tidak Ada')
                print('=============================================================')
            else:
                while True:
                    choice = input('\nApakah Anda yakin data ingin dihapus?(Y/N) : ').upper()
                    if (choice == 'Y') :
                        dataKaryawan.remove(dataKaryawan[inputHapus])
                        print('=============================================================')
                        print('\t\t\tData Deleted')
                        print('=============================================================')
                        break
                    elif (choice == 'N'):
                        print('=============================================================')
                        print('\t\t   Data Tidak Terhapus')
                        print('=============================================================')
                        break
        elif (hapusData == '2') :
            break

def tampilan_Menu() :
    print('''\n
        ---------------Data Karyawan Perusahaan---------------

        Pilihan Menu :

        1. Menampilkan Data Karyawan
        2. Menambah Data Karyawan
        3. Memperbarui Data karyawan
        4. Menghapus Data Karyawan
        5. Exit
        ''')

while True :
    tampilan_Menu()
    menuUtama = input('Masukkan angka menu yang ingin dijalankan : ')
    if (menuUtama == '1') :
        baca_Data()
    elif (menuUtama =='2') :
        tambah_Data()
    elif (menuUtama == '3') :
        perbarui_Data()
    elif (menuUtama == '4') :
        hapus_Data()
    elif (menuUtama == '5') :
        exit()
    else :
        print('\t=================================================================')
        print('\t\t\tPilihan yang Anda masukkan salah')
        print('\t=================================================================')
