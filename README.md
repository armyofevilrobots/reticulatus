    __________        __  .__             .__          __                 
    \______   \ _____/  |_|__| ____  __ __|  | _____ _/  |_ __ __  ______ 
     |       _// __ \   __\  |/ ___\|  |  \  | \__  \\   __\  |  \/  ___/ 
     |    |   \  ___/|  | |  \  \___|  |  /  |__/ __ \|  | |  |  /\___ \  
     |____|_  /\___  >__| |__|\___  >____/|____(____  /__| |____//____  > 
            \/     \/             \/                \/                \/  
     _____   _______ _  _  ___  _  _   ___ ___ ___ ___    _   ___      
    | _ \ \ / /_   _| || |/ _ \| \| | | _ \ __| _ \ _ \  /_\ | _ \     
    |  _/\ V /  | | | __ | (_) | .` | |   / _||  _/   / / _ \|  _/      
    |_|   |_|   |_| |_||_|\___/|_|\_| |_|_\___|_| |_|_\/_/ \_\_|       
      ___  ___ ___  ___  ___   __  __   _   _  _  ___ _    ___ ___      
     / __|/ __/ _ \|   \| __| |  \/  | /_\ | \| |/ __| |  | __| _ \     
    | (_ | (_| (_) | |) | _|  | |\/| |/ _ \| .` | (_ | |__| _||   /     
     \___|\___\___/|___/|___| |_|  |_/_/ \_\_|\_|\___|____|___|_|_\     

============================================
Reticulatus : A Python Reprap G-Code mangler
============================================

This is a project that will (soon) provide gcode post-processing, including
the following:

 - Shallow dome perimeter gap filling
 - Smooth transitions between layers (ramping)
 - Structural ribbing on interial walls
 - Optimized (voronoi/delaunay) infill on perimeter only objects
 - High speed optimized exterior sacrificial support
 - Corner velocity optimization via virtual G64
