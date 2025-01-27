#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 10:38:58 2025

@author: cvetkofabian
"""

from tabulate import tabulate




sem1 = {
        "pro1M": [[(5.5, 0.1), (5.8, 0.15), (4.9, 0.2), (5.3, 0.15)], [None]],
        "an1"  : [[4.6, 4.4], []],
        "mechM": [[5, 3.5, 5], []],
        "lalg1": [[4.2, 4.7], []],
        "esfss": [[(5.58, 0.6), (5.35, 0.4)], [None]],
        "AuA"  : [[(5.8, 0.5), (5.2, 0.2), (4.5, 0.3)], [None]],
        "infM" : [[(6.1, 0.5), (5.4, 0.25), (5.6, 0.25)], [None]],
        "werk" : [[5.4], [None]],
        "ch1"  : [[4.5], []],
        "hkon" : [[(4.65, 0.5), (6, 0.2)], [None]]
        }




def average(grades, round_average = False):
    if grades == [] or grades == [None] or grades == None:
        return None
    
    grades_weighted = []
    grades_weights = []
    for grade in grades:
        if type(grade) == tuple:
            grades_weights.append(grade[1])
            grade = grade[0] * grade[1]
        else:
            grades_weights.append(1)
        grades_weighted.append(grade)
    weight_total = sum(grades_weights)
    average = sum(grades_weighted) * 1/weight_total
    if round_average != False:
        return round(average, round_average)
    return average

def grades(semester):
    modules = list(semester.keys())
    results = {}
    for module in modules:
        grades_semester = semester[module][0]
        grades_final_exam = semester[module][1]
        
        average_semester = average(grades_semester, round_average=1)
        average_final_exam = average(grades_final_exam, round_average=1)
        
        averages = []
        if average_semester != None:
            averages.append(average_semester)
        if average_final_exam != None:
            averages.append(average_final_exam)
            
        if len(averages) != 0:
            average_total = sum(averages)
        else:
            average_total = None
        
        results[module] = (average_semester, average_final_exam, average_total)
    return results

def print_table(grades_dict, title = None):
    if title == None:
        title = "Modul"
    
    table = [(key, *value) for key, value in grades_dict.items()]
    headers = [title, "Erfa", "MSP", "Final"]

    print(tabulate(table, headers=headers, tablefmt="grid", colalign=("left", "right", "right", "right")))
        
    



print_table(grades(sem1), "Sem. 1")
