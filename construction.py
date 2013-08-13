import variables

# Home location
home = (variables.dim_x / 2.2, variables.dim_y / 2.2,0)
home_size = (40, 40, variables.epsilon)
home_center = tuple([h_coord + size_coord / 2 for h_coord, size_coord in 
      zip(home,home_size)])

# Location where construction is to begin
construction_location = (variables.dim_x / 2, variables.dim_y / 2,0)
construction_size = (40,40,variables.epsilon)
construction_location_center = tuple([h_coord + size_coord / 2 for h_coord, size_coord in 
      zip(construction_location,construction_size)])

# Angle Contraint : When wiggling, if no beam is found within this
# angle from the vertical, than the beam is laid at vertical_angle_set (
# which is just an angle, so no direction is actually specified)
# All angles are in degrees.
beam = {
  # The lenght of the beam
  'length'                    : variables.beam_length,

  # The minumum from vertical at which a beam is allowed to be constructed when
  # intersecting with another
  'min_angle_constraint'      : 5,

  # 
  'angle_constraint'          : 45,
  'max_angle_constraint'      : 60,
  'vertical_dir_set'          : (0,0,1),
  'joint_limit'               : 3.39,
  'beam_limit'                : 0.55,
  'horizontal_beam_limit'     : 8.3,
  'moment_change_limit'       : 0.2,
  'structure_check'           : variables.structure_check,
  'support_angle'             : 60,
  'support_angle_min'         : 35,
  'support_angle_max'         : 85,

  # This is the angle from the vertical at which a beam is initially constructed
  'construction_angle'        : 30,

  # This is the angle between the beam we want to repair and the beam we are
  # currently on.
  # If the actual angle is greater, then we add a support beam
  # If it is less, then we repair directly
  'direct_repair_limit'      : 90,

  # This is how far a support beam construction from our current beam must
  # occur in order for the beam to be considered acceptable
  'support_angle_difference' : 10,

  # If a beam is within this angle from vertical, it is considered vertical for 
  # the purpose of determining the direction we wish to travel in
  'verticality_angle'        :  10,

  # If a direction is within this angle of the direction of the beam we want to
  # repair, then we consider it a preferred location.
  'direction_tolerance_angle':  30,

  # If there is a joint within this distance of the tip, then the beam is 
  # considered to be support and no longer requires repair
  'joint_distance'           :  48 # inches
}
