import matplotlib.pyplot as plt
import networkx as nx

# Define the tables and their relationships
tables = {
    "outsource_links": [],
    "users": [],
    "password_resets": [],
    "study_languages": [],
    "class_profiles": [],
    "class_shifts": [],
    "class_types": [],
    "subjects": [],
    "education_years": [],
    "school_types": [],
    "school_kinds": [],
    "school_subjects": [],
    "region_profiles": ["parent_id"],
    "school_profiles": ["region_id", "type_id", "kind_id", "subject_id"],
    "classes": ["school_id", "education_language_id", "mother_language_id", "type_id", "profile_id", "shift_id", "education_year_id"],
    "education_plans": ["subject_id", "education_year_id"],
    "teacher_subjects": ["subject_id"],
    "schedules": ["subject_id", "class_id", "education_year_id"],
    "schedule_students": ["schedule_id"],
    "families": [],
    "parent_profiles": ["family_id", "user_id"],
    "lesson_hour_templates": ["school_id"],
    "lesson_hour_template_details": ["template_id"],
    "schedule_templates": ["subject_id", "lesson_hour_template_id", "class_id"],
    "template_students": ["template_id"],
    "class_indice_subjects": ["subject_id"],
    "moodle_courses": ["subject_id", "school_id", "class_id"],
    "holidays": [],
    "teacher_subject_details": ["subject_id", "school_id"],
    "grade_logs": [],
    "schedule_template_drafts": ["subject_id", "lesson_hour_template_id", "class_id"],
    "jobs": [],
    "log_queues": [],
    "sms_codes": [],
    "config_class_indice_exams": ["school_id", "subject_id"],
    "config_exam_scores": ["school_id"],
    "exam_total_scores": ["subject_id", "education_year_id"],
    "periods": ["education_year_id"],
    "exams": ["school_id"],
    "criterias": ["school_id", "subject_id", "education_year_id"],
    "schedule_criterias": ["schedule_id", "criteria_id"],
    "schedule_records": ["schedule_id"],
    "class_exams": ["class_id", "subject_id", "exam_id", "period_id"],
    "exam_scores": ["class_exam_id"],
    "journal_score_types": [],
    "journal_score_type_values": ["journal_score_type_id"],
    "journal_score_exchanges": ["journal_score_type_value_id"],
    "user_tokens": ["user_id"],
    "user_journal_limits": ["user_id", "school_id"],
    "school_journal_score_types": ["school_id", "period_id", "journal_score_type_id"],
    "class_subject_groups": ["class_id", "subject_id"],
    "class_subject_group_pupils": ["class_subject_group_id"],
    "activity_logs": []
}

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
for table, references in tables.items():
    G.add_node(table)
    for ref in references:
        G.add_edge(table, ref)

# Set plot size
plt.figure(figsize=(20, 15))

# Draw the graph
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', arrows=True, arrowstyle='-|>', arrowsize=15)

# Add labels to the edges
edge_labels = {edge: edge[1] for edge in G.edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=8)

# Show the plot
plt.title("ERD for Database Tables")
plt.show()
