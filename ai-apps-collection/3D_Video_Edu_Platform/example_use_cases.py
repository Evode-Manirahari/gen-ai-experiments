"""
Example use cases and configurations for the 3D Video Educational AI Platform
"""

# Physics Examples
PHYSICS_EXAMPLES = {
    "gravity_and_planetary_motion": {
        "topic": "Gravity and Planetary Motion",
        "subject": "Physics",
        "level": "High School",
        "objects": [
            {
                "type": "sphere",
                "name": "Sun",
                "location": (0, 0, 0),
                "radius": 2.0,
                "color": (1.0, 1.0, 0.0, 1.0)  # Yellow
            },
            {
                "type": "sphere",
                "name": "Earth",
                "location": (8, 0, 0),
                "radius": 0.5,
                "color": (0.0, 0.5, 1.0, 1.0)  # Blue
            },
            {
                "type": "sphere",
                "name": "Moon",
                "location": (9, 0, 0),
                "radius": 0.2,
                "color": (0.7, 0.7, 0.7, 1.0)  # Gray
            }
        ],
        "animations": [
            {
                "object": "Earth",
                "type": "orbit",
                "center": (0, 0, 0),
                "radius": 8,
                "duration": 300,
                "speed": 1.0
            },
            {
                "object": "Moon",
                "type": "orbit",
                "center": (8, 0, 0),
                "radius": 1,
                "duration": 100,
                "speed": 3.0
            }
        ],
        "camera_movements": [
            {
                "frame": 1,
                "location": (0, -15, 5),
                "rotation": (60, 0, 0)
            },
            {
                "frame": 150,
                "location": (8, -8, 3),
                "rotation": (45, 0, 0)
            },
            {
                "frame": 300,
                "location": (0, -15, 5),
                "rotation": (60, 0, 0)
            }
        ]
    },
    
    "electromagnetic_fields": {
        "topic": "Electromagnetic Fields",
        "subject": "Physics",
        "level": "College",
        "objects": [
            {
                "type": "sphere",
                "name": "Positive_Charge",
                "location": (-2, 0, 0),
                "radius": 0.3,
                "color": (1.0, 0.0, 0.0, 1.0)  # Red
            },
            {
                "type": "sphere",
                "name": "Negative_Charge",
                "location": (2, 0, 0),
                "radius": 0.3,
                "color": (0.0, 0.0, 1.0, 1.0)  # Blue
            }
        ],
        "field_lines": True,
        "animations": [
            {
                "type": "field_visualization",
                "charges": ["Positive_Charge", "Negative_Charge"],
                "duration": 300
            }
        ]
    }
}

# Chemistry Examples
CHEMISTRY_EXAMPLES = {
    "water_molecule": {
        "topic": "Water Molecule Structure",
        "subject": "Chemistry",
        "level": "High School",
        "molecules": [
            {
                "name": "H2O",
                "atoms": [
                    {
                        "element": "O",
                        "position": (0, 0, 0),
                        "radius": 0.6,
                        "color": (1.0, 0.0, 0.0, 1.0)  # Red for Oxygen
                    },
                    {
                        "element": "H",
                        "position": (0.96, 0.25, 0),
                        "radius": 0.3,
                        "color": (1.0, 1.0, 1.0, 1.0)  # White for Hydrogen
                    },
                    {
                        "element": "H",
                        "position": (0.96, -0.25, 0),
                        "radius": 0.3,
                        "color": (1.0, 1.0, 1.0, 1.0)  # White for Hydrogen
                    }
                ],
                "bonds": [
                    {
                        "id": 1,
                        "center": (0.48, 0.125, 0),
                        "length": 0.96,
                        "rotation": (0, 0, 0)
                    },
                    {
                        "id": 2,
                        "center": (0.48, -0.125, 0),
                        "length": 0.96,
                        "rotation": (0, 0, 0)
                    }
                ]
            }
        ],
        "animations": [
            {
                "type": "molecular_vibration",
                "molecule": "H2O",
                "duration": 300,
                "frequency": 2.0
            }
        ]
    },
    
    "dna_structure": {
        "topic": "DNA Double Helix Structure",
        "subject": "Chemistry",
        "level": "College",
        "molecules": [
            {
                "name": "DNA_Helix",
                "atoms": [],  # Will be generated programmatically
                "bonds": []   # Will be generated programmatically
            }
        ],
        "animations": [
            {
                "type": "helix_rotation",
                "molecule": "DNA_Helix",
                "duration": 300,
                "rotation_speed": 1.0
            }
        ]
    }
}

# Biology Examples
BIOLOGY_EXAMPLES = {
    "cell_division": {
        "topic": "Mitosis - Cell Division Process",
        "subject": "Biology",
        "level": "High School",
        "structures": [
            {
                "type": "cell",
                "name": "Parent_Cell",
                "location": (0, 0, 0),
                "radius": 3.0,
                "organelles": [
                    {
                        "name": "Nucleus",
                        "position": (0, 0, 0),
                        "radius": 1.5,
                        "color": (0.5, 0.5, 1.0, 1.0)  # Blue
                    },
                    {
                        "name": "Mitochondria",
                        "position": (1.5, 1.5, 0),
                        "radius": 0.5,
                        "color": (0.0, 1.0, 0.0, 1.0)  # Green
                    },
                    {
                        "name": "Mitochondria_2",
                        "position": (-1.5, -1.5, 0),
                        "radius": 0.5,
                        "color": (0.0, 1.0, 0.0, 1.0)  # Green
                    }
                ]
            }
        ],
        "processes": [
            {
                "name": "mitosis",
                "steps": [
                    {
                        "frame": 1,
                        "description": "Interphase - Normal cell state",
                        "transforms": {}
                    },
                    {
                        "frame": 50,
                        "description": "Prophase - Chromosomes condense",
                        "transforms": {
                            "Parent_Cell_Nucleus": {
                                "location": (0, 0, 0),
                                "rotation": (0, 0, 0),
                                "scale": (1.2, 1.2, 1.2)
                            }
                        }
                    },
                    {
                        "frame": 100,
                        "description": "Metaphase - Chromosomes align",
                        "transforms": {
                            "Parent_Cell_Nucleus": {
                                "location": (0, 0, 0),
                                "rotation": (0, 0, 0),
                                "scale": (1.5, 1.5, 1.5)
                            }
                        }
                    },
                    {
                        "frame": 150,
                        "description": "Anaphase - Chromosomes separate",
                        "transforms": {
                            "Parent_Cell_Nucleus": {
                                "location": (0, 0, 0),
                                "rotation": (0, 0, 0),
                                "scale": (2.0, 0.5, 0.5)
                            }
                        }
                    },
                    {
                        "frame": 200,
                        "description": "Telophase - Two nuclei form",
                        "transforms": {
                            "Parent_Cell_Nucleus": {
                                "location": (0, 0, 0),
                                "rotation": (0, 0, 0),
                                "scale": (1.0, 1.0, 1.0)
                            }
                        }
                    },
                    {
                        "frame": 250,
                        "description": "Cytokinesis - Cell divides",
                        "transforms": {
                            "Parent_Cell": {
                                "location": (0, 0, 0),
                                "rotation": (0, 0, 0),
                                "scale": (1.0, 0.5, 1.0)
                            }
                        }
                    }
                ]
            }
        ]
    },
    
    "photosynthesis": {
        "topic": "Photosynthesis Process",
        "subject": "Biology",
        "level": "Middle School",
        "structures": [
            {
                "type": "leaf",
                "name": "Plant_Leaf",
                "location": (0, 0, 0),
                "size": (4, 6, 0.2),
                "color": (0.0, 0.8, 0.0, 1.0)  # Green
            },
            {
                "type": "sun",
                "name": "Sunlight",
                "location": (0, 0, 8),
                "radius": 1.0,
                "color": (1.0, 1.0, 0.0, 1.0)  # Yellow
            }
        ],
        "processes": [
            {
                "name": "photosynthesis",
                "steps": [
                    {
                        "frame": 1,
                        "description": "Sunlight hits the leaf",
                        "transforms": {
                            "Sunlight": {
                                "location": (0, 0, 8),
                                "rotation": (0, 0, 0),
                                "scale": (1.0, 1.0, 1.0)
                            }
                        }
                    },
                    {
                        "frame": 100,
                        "description": "Chlorophyll absorbs light energy",
                        "transforms": {
                            "Plant_Leaf": {
                                "location": (0, 0, 0),
                                "rotation": (0, 0, 0),
                                "scale": (1.2, 1.2, 1.2)
                            }
                        }
                    },
                    {
                        "frame": 200,
                        "description": "Glucose and oxygen are produced",
                        "transforms": {
                            "Plant_Leaf": {
                                "location": (0, 0, 0),
                                "rotation": (0, 0, 0),
                                "scale": (1.0, 1.0, 1.0)
                            }
                        }
                    }
                ]
            }
        ]
    }
}

# Mathematics Examples
MATH_EXAMPLES = {
    "calculus_derivatives": {
        "topic": "Calculus - Understanding Derivatives",
        "subject": "Mathematics",
        "level": "College",
        "shapes": [
            {
                "type": "function_surface",
                "name": "Function_Curve",
                "equation": "y = x^2",
                "range": (-5, 5),
                "color": (0.0, 0.5, 1.0, 1.0)  # Blue
            },
            {
                "type": "tangent_line",
                "name": "Tangent_Line",
                "point": (2, 4),
                "slope": 4,
                "color": (1.0, 0.0, 0.0, 1.0)  # Red
            }
        ],
        "animations": [
            {
                "type": "tangent_animation",
                "function": "Function_Curve",
                "tangent": "Tangent_Line",
                "duration": 300,
                "point_movement": True
            }
        ]
    },
    
    "geometric_proofs": {
        "topic": "Pythagorean Theorem Proof",
        "subject": "Mathematics",
        "level": "High School",
        "shapes": [
            {
                "type": "geometric_solid",
                "name": "Right_Triangle",
                "shape": "custom",
                "vertices": [(0, 0, 0), (3, 0, 0), (0, 4, 0)],
                "color": (0.8, 0.8, 0.8, 1.0)  # Gray
            },
            {
                "type": "geometric_solid",
                "name": "Square_A",
                "shape": "cube",
                "location": (0, 0, 0),
                "size": 3,
                "color": (1.0, 0.0, 0.0, 0.5)  # Red, semi-transparent
            },
            {
                "type": "geometric_solid",
                "name": "Square_B",
                "shape": "cube",
                "location": (0, 0, 0),
                "size": 4,
                "color": (0.0, 1.0, 0.0, 0.5)  # Green, semi-transparent
            },
            {
                "type": "geometric_solid",
                "name": "Square_C",
                "shape": "cube",
                "location": (0, 0, 0),
                "size": 5,
                "color": (0.0, 0.0, 1.0, 0.5)  # Blue, semi-transparent
            }
        ],
        "animations": [
            {
                "type": "proof_animation",
                "shapes": ["Square_A", "Square_B", "Square_C"],
                "duration": 300,
                "demonstration": "area_equality"
            }
        ]
    }
}

# History Examples
HISTORY_EXAMPLES = {
    "ancient_rome": {
        "topic": "Ancient Roman Architecture",
        "subject": "History",
        "level": "High School",
        "structures": [
            {
                "type": "building",
                "name": "Colosseum",
                "location": (0, 0, 0),
                "size": (4, 4, 3),
                "details": [
                    {
                        "name": "Arches",
                        "position": (0, 0, 1.5),
                        "size": (0.2, 4, 1),
                        "color": (0.8, 0.7, 0.6, 1.0)  # Stone color
                    },
                    {
                        "name": "Columns",
                        "position": (1.5, 1.5, 0),
                        "size": (0.3, 0.3, 3),
                        "color": (0.9, 0.8, 0.7, 1.0)  # Marble color
                    }
                ]
            },
            {
                "type": "monument",
                "name": "Arch_of_Titus",
                "location": (6, 0, 0),
                "radius": 1,
                "height": 3
            }
        ],
        "timeline": [
            {
                "name": "construction_phase",
                "steps": [
                    {
                        "frame": 1,
                        "description": "Foundation laid",
                        "transforms": {
                            "Colosseum": {
                                "location": (0, 0, 0),
                                "rotation": (0, 0, 0),
                                "scale": (0.1, 0.1, 0.1)
                            }
                        }
                    },
                    {
                        "frame": 100,
                        "description": "Walls constructed",
                        "transforms": {
                            "Colosseum": {
                                "location": (0, 0, 0),
                                "rotation": (0, 0, 0),
                                "scale": (1.0, 1.0, 0.5)
                            }
                        }
                    },
                    {
                        "frame": 200,
                        "description": "Arches and columns added",
                        "transforms": {
                            "Colosseum": {
                                "location": (0, 0, 0),
                                "rotation": (0, 0, 0),
                                "scale": (1.0, 1.0, 1.0)
                            }
                        }
                    }
                ]
            }
        ]
    }
}

# Compile all examples
ALL_EXAMPLES = {
    "Physics": PHYSICS_EXAMPLES,
    "Chemistry": CHEMISTRY_EXAMPLES,
    "Biology": BIOLOGY_EXAMPLES,
    "Mathematics": MATH_EXAMPLES,
    "History": HISTORY_EXAMPLES
}

def get_example_by_subject(subject: str) -> dict:
    """Get all examples for a specific subject"""
    return ALL_EXAMPLES.get(subject, {})

def get_example_by_topic(subject: str, topic: str) -> dict:
    """Get a specific example by subject and topic"""
    subject_examples = get_example_by_subject(subject)
    return subject_examples.get(topic, {})

def list_all_topics() -> dict:
    """List all available topics across all subjects"""
    topics = {}
    for subject, examples in ALL_EXAMPLES.items():
        topics[subject] = list(examples.keys())
    return topics
