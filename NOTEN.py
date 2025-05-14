#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 10:38:58 2025

@author: cvetkofabian
"""




sem1 = {
        "pro1M": [[(5.5, 0.1, "Konzeptskizze"), (5.8, 0.15, "Sitzungsprotokolle"), (4.9, 0.2, "Reflexionsbericht"), (5.3, 0.15, "Fertigungszeichnung"), (5, 0.15, "Bericht Teil: Sprachkompetenz"), (4.8, 0.15, "Bericht Teil: Konstruktion"), (5.5, 0.1, "Präsentation")], [None]],
        "an1"  : [[4.6, 4.4, (5.1, 1, "Bonus +0.2 Note für Python-Aufgabe Newton-Verfahren")], [4.9]],
        "mechM": [[5, 3.5, 5], [5.2]],
        "lalg1": [[4.2, 4.7], [4.7]],
        "esfss": [[(5.58, 0.6, "Presentation"), (5.35, 0.4, "Final Exam")], [None]],
        "AuA"  : [[(5.8, 0.5, "1-Minuten-Rede"), (5.2, 0.2, "Analyse Auftritt"), (4.5, 0.3, "Podium")], [None]],
        "infM" : [[(6.1, 0.5), (5.4, 0.25, "Projekt"), (5.6, 0.25, "Projekt")], [None]],
        "werk" : [[5.4, 4.8], [None]],
        "ch1"  : [[4.5], [4.3]],
        "hkon" : [[(4.65, 0.5, "Teil Herstellung"), (6, 0.2, "Teil Konstruktion Peergrading Zeichnung"), (4.6, 0.3, "Teil Konstruktion")], [None]]
        }


sem2 = {
        "pro2M": [[(5.75, 0.1, "Sitzungsmoderation"), (4.5, 0.15, "Patentrecherche")], [None]],
        "thdM" : [[], []],
        "an2"  : [[4.9], []],
        "lalg2": [[5.2], [None]],
        "chkL" : [[(5.1, 0.25, "Chemie Schriftliche Prüfung")], [None]],
        "stk"  : [[5.18], [None]],
        "wisa" : [[], [None]],
        "wus"  : [[3.8], []],
        "mel"  : [[(3.45, 1), (4.04, 1)], [None]],
        "eidpe": [[(6, 0.2, "Moodle Exercises"), (5.5, 0.4, "Poster and Canvas")], [None]],
        "werk2": [[], []],
       }




def round_half_up(number, decimals=0):
    multiplier = 10**decimals
    return int(number * multiplier + 0.5) / multiplier


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
        return round_half_up(average, round_average)
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
            average_total = round_half_up(sum(averages) / len(averages), 1)
        else:
            average_total = None
        
        results[module] = (average_semester, average_final_exam, average_total)
    return results




def print_table_tabulate(results_dict, title = None):
    from tabulate import tabulate
    
    if title == None:
        title = "Modul"
    
    table = [(key, *value) for key, value in results_dict.items()]
    headers = [title, "Erfa", "MSP", "Final"]

    print(tabulate(table, headers=headers, tablefmt="grid", colalign=("left", "right", "right", "right")))


def print_table_rich(results_dict, title=None):
    from rich.table import Table
    from rich.console import Console
    
    console = Console()
    if title != None:
        table = Table(title=title)

    table.add_column("Modul", style="bold", justify="left")
    table.add_column("Erfa", justify="right")
    table.add_column("MSP", justify="right")
    table.add_column("Final", justify="right")

    def format_grade(val):
        if val is None:
            return "-"
        if val < 3.75:
            return f"[red]{val:.1f}[/red]"
        elif val < 4.0:
            return f"[yellow]{val:.1f}[/yellow]"
        else:
            return f"[green]{val:.1f}[/green]"

    for module, (average_semester, average_final_exam, average_total) in results_dict.items():
        table.add_row(
            module,
            format_grade(average_semester),
            format_grade(average_final_exam),
            format_grade(average_total))
    print("")
    console.print(table)




print_table_rich(grades(sem1), "Sem. 1")
print_table_rich(grades(sem2), "Sem. 2")


input("\n\nPress Enter to quit...\n")
