"""
Domain Specific Language
"""

from .core.ast import Node
from typing import Any

__all__ = [
    "MolangExpr",
    "array",
    "geometry",
    "material",
    "math",
    "query",
    "temp",
    "texture",
    "variable",
    "context",
]

class MolangExpr:
    expr: str
    def __init__(self, expr: Any) -> None: ...
    def eval(self, context: dict[str, Any]) -> Any: ...
    def parse(self) -> Node: ...
    def compile(self) -> str: ...
    @staticmethod
    def value(value: Any) -> str | MolangExpr: ...
    def __call__(self, *args) -> MolangExpr: ...
    def __invert__(self) -> MolangExpr: ...
    def __or__(self, other: Any) -> MolangExpr: ...
    def __and__(self, other: Any) -> MolangExpr: ...
    def __gt__(self, other: Any) -> MolangExpr: ...
    def __lt__(self, other: Any) -> MolangExpr: ...
    def __ge__(self, other: Any) -> MolangExpr: ...
    def __le__(self, other: Any) -> MolangExpr: ...
    def __ne__(self, other: Any) -> MolangExpr: ...  # type: ignore
    def __eq__(self, other: Any) -> MolangExpr: ...  # type: ignore
    def __add__(self, other: Any) -> MolangExpr: ...
    def __sub__(self, other: Any) -> MolangExpr: ...
    def __mul__(self, other: Any) -> MolangExpr: ...
    def __truediv__(self, other: Any) -> MolangExpr: ...
    def __floordiv__(self, other: Any) -> MolangExpr: ...
    def __getitem__(self, name: float | int | MolangExpr) -> MolangExpr: ...
    def if_(self, true_v: Any, false_v: Any) -> MolangExpr: ...
    @staticmethod
    def for_each(
        variable: MolangExpr, array: MolangExpr, expression: MolangExpr
    ) -> MolangExpr: ...
    @staticmethod
    def loop(count: int | MolangExpr, expression: MolangExpr) -> MolangExpr: ...

class VariableNamespace:
    def __call__(self, name: str, *args) -> MolangExpr: ...
    def __init__(self, prefix: str) -> None: ...
    def __getattr__(self, name: str) -> MolangExpr: ...
    def __setattr__(self, name: str, value: Any) -> None: ...

class ArrayNamespace:
    def __getattr__(self, name: str) -> MolangExpr: ...

class MathNamespace(VariableNamespace):
    def abs(self, value) -> MolangExpr: ...
    def acos(self, value) -> MolangExpr: ...
    def asin(self, value) -> MolangExpr: ...
    def atan(self, value) -> MolangExpr: ...
    def atan2(self, y, x) -> MolangExpr: ...
    def ceil(self, value) -> MolangExpr: ...
    def clamp(self, value, min, max) -> MolangExpr: ...
    def copy_sign(self, A, B) -> MolangExpr: ...
    def cos(self, value) -> MolangExpr: ...
    def die_roll(self, num, low, high) -> MolangExpr: ...
    def die_roll_integer(self, num, low, high) -> MolangExpr: ...
    def ease_in_back(self, start, end, value) -> MolangExpr: ...
    def ease_in_bounce(self, start, end, value) -> MolangExpr: ...
    def ease_in_circ(self, start, end, value) -> MolangExpr: ...
    def ease_in_cubic(self, start, end, value) -> MolangExpr: ...
    def ease_in_elastic(self, start, end, value) -> MolangExpr: ...
    def ease_in_expo(self, start, end, value) -> MolangExpr: ...
    def ease_in_out_back(self, start, end, value) -> MolangExpr: ...
    def ease_in_out_bounce(self, start, end, value) -> MolangExpr: ...
    def ease_in_out_circ(self, start, end, value) -> MolangExpr: ...
    def ease_in_out_cubic(self, start, end, value) -> MolangExpr: ...
    def ease_in_out_elastic(self, start, end, value) -> MolangExpr: ...
    def ease_in_out_expo(self, start, end, value) -> MolangExpr: ...
    def ease_in_out_quad(self, start, end, value) -> MolangExpr: ...
    def ease_in_out_quart(self, start, end, value) -> MolangExpr: ...
    def ease_in_out_quint(self, start, end, value) -> MolangExpr: ...
    def ease_in_out_sine(self, start, end, value) -> MolangExpr: ...
    def ease_in_quad(self, start, end, value) -> MolangExpr: ...
    def ease_in_quart(self, start, end, value) -> MolangExpr: ...
    def ease_in_quint(self, start, end, value) -> MolangExpr: ...
    def ease_in_sine(self, start, end, value) -> MolangExpr: ...
    def ease_out_back(self, start, end, value) -> MolangExpr: ...
    def ease_out_bounce(self, start, end, value) -> MolangExpr: ...
    def ease_out_circ(self, start, end, value) -> MolangExpr: ...
    def ease_out_cubic(self, start, end, value) -> MolangExpr: ...
    def ease_out_elastic(self, start, end, value) -> MolangExpr: ...
    def ease_out_expo(self, start, end, value) -> MolangExpr: ...
    def ease_out_quad(self, start, end, value) -> MolangExpr: ...
    def ease_out_quart(self, start, end, value) -> MolangExpr: ...
    def ease_out_quint(self, start, end, value) -> MolangExpr: ...
    def ease_out_sine(self, start, end, value) -> MolangExpr: ...
    def exp(self, value) -> MolangExpr: ...
    def floor(self, value) -> MolangExpr: ...
    def hermite_blend(self, value) -> MolangExpr: ...
    def inverse_lerp(self, start, end, value) -> MolangExpr: ...
    def lerp(self, start, end, value) -> MolangExpr: ...
    def lerprotate(self, start, end, value) -> MolangExpr: ...
    def ln(self, value) -> MolangExpr: ...
    def max(self, A, B) -> MolangExpr: ...
    def min(self, A, B) -> MolangExpr: ...
    def min_angle(self, value) -> MolangExpr: ...
    def mod(self, value, denominator) -> MolangExpr: ...
    def pow(self, base, exponent) -> MolangExpr: ...
    def random(self, low, high) -> MolangExpr: ...
    def random_integer(self, low, high) -> MolangExpr: ...
    def round(self, value) -> MolangExpr: ...
    def sign(self, value) -> MolangExpr: ...
    def sin(self, value) -> MolangExpr: ...
    def sqrt(self, value) -> MolangExpr: ...
    def trunc(self, value) -> MolangExpr: ...

    pi: MolangExpr

class QueryNamespace(VariableNamespace):
    def block_state(self, name: str) -> MolangExpr: ...
    def equipped_item_all_tags(self, slot: str, *tag: str) -> MolangExpr: ...
    def equipped_item_any_tag(self, slot: str, *tag: str) -> MolangExpr: ...
    def get_nearby_entities(self, count: int, type_id: str) -> MolangExpr: ...

    above_top_solid: MolangExpr
    actor_count: MolangExpr
    all: MolangExpr
    all_animations_finished: MolangExpr
    all_tags: MolangExpr
    anger_level: MolangExpr
    anim_time: MolangExpr
    any: MolangExpr
    any_animation_finished: MolangExpr
    any_tag: MolangExpr
    approx_eq: MolangExpr
    armor_color_slot: MolangExpr
    armor_damage_slot: MolangExpr
    armor_material_slot: MolangExpr
    armor_texture_slot: MolangExpr
    average_frame_time: MolangExpr
    base_swing_duration: MolangExpr
    block_face: MolangExpr
    block_has_all_tags: MolangExpr
    block_has_any_tag: MolangExpr
    block_neighbor_has_all_tags: MolangExpr
    block_neighbor_has_any_tag: MolangExpr
    block_property: MolangExpr
    blocking: MolangExpr
    body_x_rotation: MolangExpr
    body_y_rotation: MolangExpr
    bone_aabb: MolangExpr
    bone_orientation_matrix: MolangExpr
    bone_orientation_trs: MolangExpr
    bone_origin: MolangExpr
    bone_rotation: MolangExpr
    camera_distance_range_lerp: MolangExpr
    camera_rotation: MolangExpr
    can_climb: MolangExpr
    can_damage_nearby_mobs: MolangExpr
    can_dash: MolangExpr
    can_fly: MolangExpr
    can_power_jump: MolangExpr
    can_swim: MolangExpr
    can_walk: MolangExpr
    cape_flap_amount: MolangExpr
    cardinal_block_face_placed_on: MolangExpr
    cardinal_facing: MolangExpr
    cardinal_facing_2d: MolangExpr
    cardinal_player_facing: MolangExpr
    client_max_render_distance: MolangExpr
    client_memory_tier: MolangExpr
    combine_entities: MolangExpr
    cooldown_time: MolangExpr
    cooldown_time_remaining: MolangExpr
    count: MolangExpr
    current_squish_value: MolangExpr
    dash_cooldown_progress: MolangExpr
    day: MolangExpr
    death_ticks: MolangExpr
    debug_output: MolangExpr
    delta_time: MolangExpr
    distance_from_camera: MolangExpr
    effect_emitter_count: MolangExpr
    effect_particle_count: MolangExpr
    entity_biome_has_all_tags: MolangExpr
    entity_biome_has_any_identifier: MolangExpr
    entity_biome_has_any_tags: MolangExpr
    equipment_count: MolangExpr
    equipped_item_is_attachable: MolangExpr
    eye_target_x_rotation: MolangExpr
    eye_target_y_rotation: MolangExpr
    facing_target_to_range_attack: MolangExpr
    frame_alpha: MolangExpr
    get_actor_info_id: MolangExpr
    get_animation_frame: MolangExpr
    get_default_bone_pivot: MolangExpr
    get_equipped_item_name: MolangExpr
    get_locator_offset: MolangExpr
    get_name: MolangExpr
    get_pack_setting: MolangExpr
    get_root_locator_offset: MolangExpr
    graphics_mode_is_any: MolangExpr
    ground_speed: MolangExpr
    had_component_group: MolangExpr
    has_any_family: MolangExpr
    has_any_leashed_entity_of_type: MolangExpr
    has_armor_slot: MolangExpr
    has_biome_tag: MolangExpr
    has_block_property: MolangExpr
    has_block_state: MolangExpr
    has_cape: MolangExpr
    has_collision: MolangExpr
    has_dash_cooldown: MolangExpr
    has_gravity: MolangExpr
    has_head_gear: MolangExpr
    has_owner: MolangExpr
    has_player_rider: MolangExpr
    has_property: MolangExpr
    has_rider: MolangExpr
    has_target: MolangExpr
    head_roll_angle: MolangExpr
    head_x_rotation: MolangExpr
    head_y_rotation: MolangExpr
    health: MolangExpr
    heartbeat_interval: MolangExpr
    heartbeat_phase: MolangExpr
    heightmap: MolangExpr
    hurt_direction: MolangExpr
    hurt_time: MolangExpr
    in_range: MolangExpr
    invulnerable_ticks: MolangExpr
    is_admiring: MolangExpr
    is_alive: MolangExpr
    is_angry: MolangExpr
    is_attached: MolangExpr
    is_attached_to_entity: MolangExpr
    is_avoiding_block: MolangExpr
    is_avoiding_mobs: MolangExpr
    is_baby: MolangExpr
    is_breathing: MolangExpr
    is_bribed: MolangExpr
    is_carrying_block: MolangExpr
    is_casting: MolangExpr
    is_celebrating: MolangExpr
    is_celebrating_special: MolangExpr
    is_charged: MolangExpr
    is_charging: MolangExpr
    is_chested: MolangExpr
    is_cooldown_category: MolangExpr
    is_crawling: MolangExpr
    is_critical: MolangExpr
    is_croaking: MolangExpr
    is_dancing: MolangExpr
    is_delayed_attacking: MolangExpr
    is_digging: MolangExpr
    is_eating: MolangExpr
    is_eating_mob: MolangExpr
    is_elder: MolangExpr
    is_emerging: MolangExpr
    is_emoting: MolangExpr
    is_enchanted: MolangExpr
    is_feeling_happy: MolangExpr
    is_fire_immune: MolangExpr
    is_first_person: MolangExpr
    is_ghost: MolangExpr
    is_gliding: MolangExpr
    is_grazing: MolangExpr
    is_idling: MolangExpr
    is_ignited: MolangExpr
    is_illager_captain: MolangExpr
    is_in_contact_with_water: MolangExpr
    is_in_lava: MolangExpr
    is_in_love: MolangExpr
    is_in_ui: MolangExpr
    is_in_water: MolangExpr
    is_in_water_or_rain: MolangExpr
    is_interested: MolangExpr
    is_invisible: MolangExpr
    is_item_equipped: MolangExpr
    is_item_name_any: MolangExpr
    is_jump_goal_jumping: MolangExpr
    is_jumping: MolangExpr
    is_laying_down: MolangExpr
    is_laying_egg: MolangExpr
    is_leashed: MolangExpr
    is_levitating: MolangExpr
    is_lingering: MolangExpr
    is_local_player: MolangExpr
    is_moving: MolangExpr
    is_name_any: MolangExpr
    is_on_fire: MolangExpr
    is_on_ground: MolangExpr
    is_on_screen: MolangExpr
    is_onfire: MolangExpr
    is_orphaned: MolangExpr
    is_owner_identifier_any: MolangExpr
    is_pack_setting_enabled: MolangExpr
    is_pack_setting_selected: MolangExpr
    is_persona_or_premium_skin: MolangExpr
    is_playing_dead: MolangExpr
    is_powered: MolangExpr
    is_pregnant: MolangExpr
    is_ram_attacking: MolangExpr
    is_resting: MolangExpr
    is_riding: MolangExpr
    is_riding_any_entity_of_type: MolangExpr
    is_rising: MolangExpr
    is_roaring: MolangExpr
    is_rolling: MolangExpr
    is_saddled: MolangExpr
    is_scared: MolangExpr
    is_scenting: MolangExpr
    is_searching: MolangExpr
    is_selected_item: MolangExpr
    is_shaking: MolangExpr
    is_shaking_wetness: MolangExpr
    is_sheared: MolangExpr
    is_shield_powered: MolangExpr
    is_silent: MolangExpr
    is_sitting: MolangExpr
    is_sleeping: MolangExpr
    is_sneaking: MolangExpr
    is_sneezing: MolangExpr
    is_sniffing: MolangExpr
    is_sonic_boom: MolangExpr
    is_spectator: MolangExpr
    is_sprinting: MolangExpr
    is_stackable: MolangExpr
    is_stalking: MolangExpr
    is_standing: MolangExpr
    is_stunned: MolangExpr
    is_swimming: MolangExpr
    is_tamed: MolangExpr
    is_transforming: MolangExpr
    is_using_item: MolangExpr
    is_wall_climbing: MolangExpr
    item_in_use_duration: MolangExpr
    item_is_charged: MolangExpr
    item_max_use_duration: MolangExpr
    item_remaining_use_duration: MolangExpr
    item_slot_to_bone_name: MolangExpr
    key_frame_lerp_time: MolangExpr
    kinetic_weapon_damage_duration: MolangExpr
    kinetic_weapon_delay: MolangExpr
    kinetic_weapon_dismount_duration: MolangExpr
    kinetic_weapon_knockback_duration: MolangExpr
    last_frame_time: MolangExpr
    last_hit_by_player: MolangExpr
    last_input_mode_is_any: MolangExpr
    leashed_entity_count: MolangExpr
    lie_amount: MolangExpr
    life_span: MolangExpr
    life_time: MolangExpr
    lod_index: MolangExpr
    log: MolangExpr
    main_hand_item_max_duration: MolangExpr
    main_hand_item_use_duration: MolangExpr
    mark_variant: MolangExpr
    max_durability: MolangExpr
    max_health: MolangExpr
    max_trade_tier: MolangExpr
    maximum_frame_time: MolangExpr
    minimum_frame_time: MolangExpr
    model_scale: MolangExpr
    modified_distance_moved: MolangExpr
    modified_move_speed: MolangExpr
    modified_swing_duration: MolangExpr
    moon_brightness: MolangExpr
    moon_phase: MolangExpr
    movement_direction: MolangExpr
    noise: MolangExpr
    on_fire_time: MolangExpr
    out_of_control: MolangExpr
    overlay_alpha: MolangExpr
    owner_identifier: MolangExpr
    player_level: MolangExpr
    position: MolangExpr
    position_delta: MolangExpr
    previous_squish_value: MolangExpr
    relative_block_has_all_tags: MolangExpr
    relative_block_has_any_tag: MolangExpr
    remaining_durability: MolangExpr
    ride_body_x_rotation: MolangExpr
    ride_body_y_rotation: MolangExpr
    ride_head_x_rotation: MolangExpr
    ride_head_y_rotation: MolangExpr
    rider_body_x_rotation: MolangExpr
    rider_body_y_rotation: MolangExpr
    rider_head_x_rotation: MolangExpr
    rider_head_y_rotation: MolangExpr
    roll_counter: MolangExpr
    rotation_to_camera: MolangExpr
    scoreboard: MolangExpr
    server_memory_tier: MolangExpr
    shake_angle: MolangExpr
    shake_time: MolangExpr
    shield_blocking_bob: MolangExpr
    show_bottom: MolangExpr
    sit_amount: MolangExpr
    skin_id: MolangExpr
    sleep_rotation: MolangExpr
    sneeze_counter: MolangExpr
    spellcolor: MolangExpr
    standing_scale: MolangExpr
    state_time: MolangExpr
    structural_integrity: MolangExpr
    surface_particle_color: MolangExpr
    surface_particle_texture_coordinate: MolangExpr
    surface_particle_texture_size: MolangExpr
    swell_amount: MolangExpr
    swelling_dir: MolangExpr
    swim_amount: MolangExpr
    tail_angle: MolangExpr
    target_x_rotation: MolangExpr
    target_y_rotation: MolangExpr
    texture_frame_index: MolangExpr
    ticks_since_last_kinetic_weapon_hit: MolangExpr
    time_of_day: MolangExpr
    time_since_last_vibration_detection: MolangExpr
    time_stamp: MolangExpr
    timer_flag_1: MolangExpr
    timer_flag_2: MolangExpr
    timer_flag_3: MolangExpr
    total_emitter_count: MolangExpr
    total_particle_count: MolangExpr
    touch_only_affects_hotbar: MolangExpr
    trade_tier: MolangExpr
    unhappy_counter: MolangExpr
    variant: MolangExpr
    vertical_speed: MolangExpr
    walk_distance: MolangExpr
    wing_flap_position: MolangExpr
    wing_flap_speed: MolangExpr
    yaw_speed: MolangExpr

variable: VariableNamespace
temp: VariableNamespace
context: VariableNamespace
geometry: VariableNamespace
texture: VariableNamespace
material: VariableNamespace
query: QueryNamespace
array: ArrayNamespace
math: MathNamespace
