"""
Blender Python API templates for 3D educational video generation
"""

def create_physics_scene(topic: str, objects: list, animations: list) -> str:
    """Create a Blender scene for physics topics"""
    
    template = f'''
import bpy
import bmesh
from mathutils import Vector
import math

# Clear existing mesh objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Set up scene
scene = bpy.context.scene
scene.frame_start = 1
scene.frame_end = 300  # 10 seconds at 30fps

# Set up camera
bpy.ops.object.camera_add(location=(0, -10, 5))
camera = bpy.context.object
camera.rotation_euler = (math.radians(60), 0, 0)
scene.camera = camera

# Set up lighting
bpy.ops.object.light_add(type='SUN', location=(5, 5, 10))
sun = bpy.context.object
sun.data.energy = 3

# Add area light for better illumination
bpy.ops.object.light_add(type='AREA', location=(-5, -5, 8))
area_light = bpy.context.object
area_light.data.energy = 2
area_light.data.size = 5

# Create educational objects based on topic
{topic}_objects = {objects}

for obj_data in {topic}_objects:
    if obj_data['type'] == 'sphere':
        bpy.ops.mesh.primitive_uv_sphere_add(
            location=obj_data['location'],
            radius=obj_data['radius']
        )
        obj = bpy.context.object
        obj.name = obj_data['name']
        
        # Add material
        mat = bpy.data.materials.new(name=f"{{obj_data['name']}}_material")
        mat.use_nodes = True
        mat.node_tree.nodes["Principled BSDF"].inputs[0].default_value = obj_data['color']
        obj.data.materials.append(mat)
        
    elif obj_data['type'] == 'cube':
        bpy.ops.mesh.primitive_cube_add(
            location=obj_data['location'],
            size=obj_data['size']
        )
        obj = bpy.context.object
        obj.name = obj_data['name']
        
        # Add material
        mat = bpy.data.materials.new(name=f"{{obj_data['name']}}_material")
        mat.use_nodes = True
        mat.node_tree.nodes["Principled BSDF"].inputs[0].default_value = obj_data['color']
        obj.data.materials.append(mat)

# Add animations
{animations}

# Set up rendering
scene.render.engine = 'CYCLES'
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.fps = 30
scene.render.filepath = "/tmp/3d_edu_video/"

# Render animation
bpy.ops.render.render(animation=True)
'''
    
    return template

def create_chemistry_scene(topic: str, molecules: list, reactions: list) -> str:
    """Create a Blender scene for chemistry topics"""
    
    template = f'''
import bpy
import bmesh
from mathutils import Vector
import math

# Clear existing mesh objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Set up scene
scene = bpy.context.scene
scene.frame_start = 1
scene.frame_end = 300

# Set up camera
bpy.ops.object.camera_add(location=(0, -8, 4))
camera = bpy.context.object
camera.rotation_euler = (math.radians(45), 0, 0)
scene.camera = camera

# Set up lighting
bpy.ops.object.light_add(type='SUN', location=(3, 3, 8))
sun = bpy.context.object
sun.data.energy = 2

# Create molecular structures
molecules = {molecules}

for mol_data in molecules:
    # Create atom spheres
    for atom in mol_data['atoms']:
        bpy.ops.mesh.primitive_uv_sphere_add(
            location=atom['position'],
            radius=atom['radius']
        )
        atom_obj = bpy.context.object
        atom_obj.name = f"{{mol_data['name']}}_{{atom['element']}}"
        
        # Add material based on element
        mat = bpy.data.materials.new(name=f"{{atom['element']}}_material")
        mat.use_nodes = True
        mat.node_tree.nodes["Principled BSDF"].inputs[0].default_value = atom['color']
        atom_obj.data.materials.append(mat)
    
    # Create bonds
    for bond in mol_data['bonds']:
        bpy.ops.mesh.primitive_cylinder_add(
            location=bond['center'],
            radius=0.1
        )
        bond_obj = bpy.context.object
        bond_obj.name = f"{{mol_data['name']}}_bond_{{bond['id']}}"
        
        # Scale and rotate bond
        bond_obj.scale = (1, 1, bond['length'] / 2)
        bond_obj.rotation_euler = bond['rotation']
        
        # Add bond material
        mat = bpy.data.materials.new(name="bond_material")
        mat.use_nodes = True
        mat.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.5, 0.5, 0.5, 1)
        bond_obj.data.materials.append(mat)

# Add reaction animations
reactions = {reactions}

for reaction in reactions:
    # Animate molecular interactions
    for step in reaction['steps']:
        frame = step['frame']
        
        for obj_name, transform in step['transforms'].items():
            obj = bpy.data.objects.get(obj_name)
            if obj:
                obj.location = transform['location']
                obj.rotation_euler = transform['rotation']
                obj.keyframe_insert(data_path="location", frame=frame)
                obj.keyframe_insert(data_path="rotation_euler", frame=frame)

# Set up rendering
scene.render.engine = 'CYCLES'
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.fps = 30
scene.render.filepath = "/tmp/3d_edu_video/"

# Render animation
bpy.ops.render.render(animation=True)
'''
    
    return template

def create_biology_scene(topic: str, structures: list, processes: list) -> str:
    """Create a Blender scene for biology topics"""
    
    template = f'''
import bpy
import bmesh
from mathutils import Vector
import math

# Clear existing mesh objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Set up scene
scene = bpy.context.scene
scene.frame_start = 1
scene.frame_end = 300

# Set up camera
bpy.ops.object.camera_add(location=(0, -6, 3))
camera = bpy.context.object
camera.rotation_euler = (math.radians(30), 0, 0)
scene.camera = camera

# Set up lighting
bpy.ops.object.light_add(type='SUN', location=(2, 2, 6))
sun = bpy.context.object
sun.data.energy = 2.5

# Create biological structures
structures = {structures}

for struct_data in structures:
    if struct_data['type'] == 'cell':
        # Create cell membrane
        bpy.ops.mesh.primitive_uv_sphere_add(
            location=struct_data['location'],
            radius=struct_data['radius']
        )
        cell = bpy.context.object
        cell.name = struct_data['name']
        
        # Add semi-transparent material
        mat = bpy.data.materials.new(name="cell_membrane")
        mat.use_nodes = True
        mat.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.8, 0.9, 1.0, 0.3)
        mat.node_tree.nodes["Principled BSDF"].inputs[19].default_value = 0.3  # Alpha
        cell.data.materials.append(mat)
        
        # Create organelles
        for organelle in struct_data['organelles']:
            bpy.ops.mesh.primitive_uv_sphere_add(
                location=organelle['position'],
                radius=organelle['radius']
            )
            org = bpy.context.object
            org.name = f"{{struct_data['name']}}_{{organelle['name']}}"
            
            # Add organelle material
            mat = bpy.data.materials.new(name=f"{{organelle['name']}}_material")
            mat.use_nodes = True
            mat.node_tree.nodes["Principled BSDF"].inputs[0].default_value = organelle['color']
            org.data.materials.append(mat)
    
    elif struct_data['type'] == 'dna':
        # Create DNA double helix
        for i in range(struct_data['length']):
            # Create base pairs
            bpy.ops.mesh.primitive_cylinder_add(
                location=(math.cos(i * 0.5) * 0.5, i * 0.2, 0),
                radius=0.1
            )
            base1 = bpy.context.object
            base1.name = f"dna_base1_{{i}}"
            
            bpy.ops.mesh.primitive_cylinder_add(
                location=(math.cos(i * 0.5 + math.pi) * 0.5, i * 0.2, 0),
                radius=0.1
            )
            base2 = bpy.context.object
            base2.name = f"dna_base2_{{i}}"
            
            # Add materials
            mat1 = bpy.data.materials.new(name="dna_base1")
            mat1.use_nodes = True
            mat1.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (1, 0.5, 0.5, 1)
            base1.data.materials.append(mat1)
            
            mat2 = bpy.data.materials.new(name="dna_base2")
            mat2.use_nodes = True
            mat2.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.5, 0.5, 1, 1)
            base2.data.materials.append(mat2)

# Add process animations
processes = {processes}

for process in processes:
    for step in process['steps']:
        frame = step['frame']
        
        for obj_name, transform in step['transforms'].items():
            obj = bpy.data.objects.get(obj_name)
            if obj:
                obj.location = transform['location']
                obj.rotation_euler = transform['rotation']
                obj.scale = transform['scale']
                obj.keyframe_insert(data_path="location", frame=frame)
                obj.keyframe_insert(data_path="rotation_euler", frame=frame)
                obj.keyframe_insert(data_path="scale", frame=frame)

# Set up rendering
scene.render.engine = 'CYCLES'
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.fps = 30
scene.render.filepath = "/tmp/3d_edu_video/"

# Render animation
bpy.ops.render.render(animation=True)
'''
    
    return template

def create_mathematics_scene(topic: str, shapes: list, equations: list) -> str:
    """Create a Blender scene for mathematics topics"""
    
    template = f'''
import bpy
import bmesh
from mathutils import Vector
import math

# Clear existing mesh objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Set up scene
scene = bpy.context.scene
scene.frame_start = 1
scene.frame_end = 300

# Set up camera
bpy.ops.object.camera_add(location=(0, -8, 5))
camera = bpy.context.object
camera.rotation_euler = (math.radians(45), 0, 0)
scene.camera = camera

# Set up lighting
bpy.ops.object.light_add(type='SUN', location=(3, 3, 8))
sun = bpy.context.object
sun.data.energy = 2

# Create mathematical shapes
shapes = {shapes}

for shape_data in shapes:
    if shape_data['type'] == 'function_surface':
        # Create function surface using geometry nodes
        bpy.ops.mesh.primitive_plane_add(size=10)
        plane = bpy.context.object
        plane.name = shape_data['name']
        
        # Add geometry nodes modifier
        modifier = plane.modifiers.new(name="FunctionSurface", type='NODES')
        
        # Create geometry node group
        node_group = bpy.data.node_groups.new(name="FunctionSurface", type='GeometryNodeTree')
        
        # Add nodes for function evaluation
        input_node = node_group.nodes.new('GeometryNodeGroupInput')
        output_node = node_group.nodes.new('GeometryNodeGroupOutput')
        
        # Add math nodes for function
        math_node = node_group.nodes.new('ShaderNodeMath')
        math_node.operation = 'SINE'
        
        # Connect nodes
        node_group.links.new(input_node.outputs[0], math_node.inputs[0])
        node_group.links.new(math_node.outputs[0], output_node.inputs[0])
        
        modifier.node_group = node_group
        
    elif shape_data['type'] == 'geometric_solid':
        if shape_data['shape'] == 'cube':
            bpy.ops.mesh.primitive_cube_add(
                location=shape_data['location'],
                size=shape_data['size']
            )
        elif shape_data['shape'] == 'sphere':
            bpy.ops.mesh.primitive_uv_sphere_add(
                location=shape_data['location'],
                radius=shape_data['radius']
            )
        elif shape_data['shape'] == 'cylinder':
            bpy.ops.mesh.primitive_cylinder_add(
                location=shape_data['location'],
                radius=shape_data['radius'],
                depth=shape_data['height']
            )
        
        obj = bpy.context.object
        obj.name = shape_data['name']
        
        # Add material
        mat = bpy.data.materials.new(name=f"{{shape_data['name']}}_material")
        mat.use_nodes = True
        mat.node_tree.nodes["Principled BSDF"].inputs[0].default_value = shape_data['color']
        obj.data.materials.append(mat)

# Add equation animations
equations = {equations}

for equation in equations:
    for step in equation['steps']:
        frame = step['frame']
        
        for obj_name, transform in step['transforms'].items():
            obj = bpy.data.objects.get(obj_name)
            if obj:
                obj.location = transform['location']
                obj.rotation_euler = transform['rotation']
                obj.scale = transform['scale']
                obj.keyframe_insert(data_path="location", frame=frame)
                obj.keyframe_insert(data_path="rotation_euler", frame=frame)
                obj.keyframe_insert(data_path="scale", frame=frame)

# Set up rendering
scene.render.engine = 'CYCLES'
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.fps = 30
scene.render.filepath = "/tmp/3d_edu_video/"

# Render animation
bpy.ops.render.render(animation=True)
'''
    
    return template

def create_history_scene(topic: str, structures: list, timeline: list) -> str:
    """Create a Blender scene for history topics"""
    
    template = f'''
import bpy
import bmesh
from mathutils import Vector
import math

# Clear existing mesh objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Set up scene
scene = bpy.context.scene
scene.frame_start = 1
scene.frame_end = 300

# Set up camera
bpy.ops.object.camera_add(location=(0, -10, 8))
camera = bpy.context.object
camera.rotation_euler = (math.radians(30), 0, 0)
scene.camera = camera

# Set up lighting
bpy.ops.object.light_add(type='SUN', location=(5, 5, 10))
sun = bpy.context.object
sun.data.energy = 3

# Create historical structures
structures = {structures}

for struct_data in structures:
    if struct_data['type'] == 'building':
        # Create building base
        bpy.ops.mesh.primitive_cube_add(
            location=struct_data['location'],
            size=struct_data['size']
        )
        building = bpy.context.object
        building.name = struct_data['name']
        
        # Add architectural details
        for detail in struct_data['details']:
            bpy.ops.mesh.primitive_cube_add(
                location=detail['position'],
                size=detail['size']
            )
            detail_obj = bpy.context.object
            detail_obj.name = f"{{struct_data['name']}}_{{detail['name']}}"
            
            # Add material
            mat = bpy.data.materials.new(name=f"{{detail['name']}}_material")
            mat.use_nodes = True
            mat.node_tree.nodes["Principled BSDF"].inputs[0].default_value = detail['color']
            detail_obj.data.materials.append(mat)
    
    elif struct_data['type'] == 'monument':
        # Create monument
        bpy.ops.mesh.primitive_cylinder_add(
            location=struct_data['location'],
            radius=struct_data['radius'],
            depth=struct_data['height']
        )
        monument = bpy.context.object
        monument.name = struct_data['name']
        
        # Add material
        mat = bpy.data.materials.new(name="monument_material")
        mat.use_nodes = True
        mat.node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.8, 0.7, 0.6, 1)
        monument.data.materials.append(mat)

# Add timeline animations
timeline = {timeline}

for event in timeline:
    for step in event['steps']:
        frame = step['frame']
        
        for obj_name, transform in step['transforms'].items():
            obj = bpy.data.objects.get(obj_name)
            if obj:
                obj.location = transform['location']
                obj.rotation_euler = transform['rotation']
                obj.scale = transform['scale']
                obj.keyframe_insert(data_path="location", frame=frame)
                obj.keyframe_insert(data_path="rotation_euler", frame=frame)
                obj.keyframe_insert(data_path="scale", frame=frame)

# Set up rendering
scene.render.engine = 'CYCLES'
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.fps = 30
scene.render.filepath = "/tmp/3d_edu_video/"

# Render animation
bpy.ops.render.render(animation=True)
'''
    
    return template
