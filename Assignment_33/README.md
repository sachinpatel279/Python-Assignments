# Duplicate File Removal Automation

## 1. Project Description

This project is developed using Python.

The automation script periodically scans a specified directory, identifies duplicate files using MD5 checksum, deletes duplicate copies, creates a timestamp-based log file, and sends the log file through email.

---

# 2. Features

- Recursive Directory Scanning
- MD5 Checksum Based Duplicate Detection
- Automatic Duplicate File Removal
- Keep Original File
- Delete Duplicate Copies
- Timestamp Based Log Generation
- Log File Creation inside Marvellous Folder
- Periodic Execution using Schedule Module
- Email Notification
- Log File Attachment
- Input Validation
- Exception Handling
- Help Option
- Usage Option

---

# 3. Requirements

- Python 3.14
- Internet Connection
- Gmail Account
- Gmail App Password
- schedule module

Install schedule module

```bash
pip install schedule
```

---

# 4. Project Structure

```
Assignment_33/
│
├── Duplicate.py
├── MailSender.py
├── DuplicateFileRemoval.py
├── README.md
└── Marvellous/
        DuplicateRemovalLog_Date_Time.log
```

---

# 5. Command Line Options

Argument 1

Directory Path

Example

```
E:/Data/Demo
```

Argument 2

Time Interval (Minutes)

Example

```
50
```

Argument 3

Receiver Email Address

Example

```
marvellousinfosystem@gmail.com
```

---

# 6. Execution Command

```
python DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com
```

---

# 7. Help Command

```
python DuplicateFileRemoval.py --help
```

or

```
python DuplicateFileRemoval.py -h
```

---

# 8. Usage Command

```
python DuplicateFileRemoval.py --usage
```

or

```
python DuplicateFileRemoval.py -u
```

---

# 9. Log File Information

Log files are stored inside

```
Marvellous
```

folder.

Example

```
DuplicateRemovalLog_20_07_2026_23_30_15.log
```

Log File contains

- Starting Time
- Completion Time
- Directory Name
- Total Files Scanned
- Duplicate Files Found
- Duplicate Files Deleted
- Deleted File Paths
- Checksum Values
- Errors
- Email Delivery Status

---

# 10. Email Configuration

Configure

- Sender Email
- Gmail App Password

The log file is attached with every email.

Email Body contains

- Starting Time
- Completion Time
- Directory Name
- Total Files
- Duplicate Files Found
- Duplicate Files Deleted

---

# 11. Important Notes

- Deleted files may not be recoverable.
- Testing should first be performed on a sample directory.
- Email passwords should not be hard-coded.
- The first file from each duplicate group should be preserved.
- Files should be considered duplicates only when their checksums are identical
---

# 12. Expected Output

After every scheduled execution

- Duplicate files should be removed from the supplied directory.
- One original file from every duplicate group should remain.
- A timestamp-based log file should be created inside the Marvellous directory.
- The log file should contain the details of all deleted files.
- Operation statistics should be recorded.
- The log file should be sent to the receiver through email.
- The operation should repeat after the specified interval.
---

# Author

Sachin Nemaram Patel
