from enum import Enum
from typing import List

class ReportType(Enum):
    UNSAFE = 0
    SAFE = 1

def validate_report_simple(report: List[int]) -> Enum:
    if report[1] > report[0]:
        report.reverse()
    
    for i in range(1, len(report)):
        diff = report[i-1] - report[i]
        if diff < 1 or diff > 3:
            return ReportType.UNSAFE
        
    return ReportType.SAFE


def validate_report_pd(report: List[int]) -> Enum:
    if validate_report_simple(report) == ReportType.SAFE:
        return ReportType.SAFE
    
    for i in range(len(report)):
        copy = report.copy()
        copy.pop(i)
        if validate_report_simple(copy) == ReportType.SAFE:
            return ReportType.SAFE
        
    return ReportType.UNSAFE