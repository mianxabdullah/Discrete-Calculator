"""
Discrete Structures Calculator - Enhanced GUI Application
A comprehensive calculator implementing number systems, set operations, 
searching, and sorting algorithms with modern, interactive UI.
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from number_systems import NumberSystemConverter
from set_operations import SetOperations
from searching import SearchingAlgorithms
from sorting import SortingAlgorithms
import time


class ModernButton(tk.Button):
    """Custom button with hover effects."""
    def __init__(self, parent, **kwargs):
        self.original_bg = kwargs.get('bg', '#3498db')
        self.hover_bg = kwargs.get('hover_bg', self.darken_color(self.original_bg))
        kwargs.pop('hover_bg', None)
        super().__init__(parent, **kwargs)
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)
        self.bind('<Button-1>', self.on_click)
    
    def darken_color(self, color):
        """Darken a hex color."""
        if color.startswith('#'):
            rgb = tuple(int(color[i:i+2], 16) for i in (1, 3, 5))
            rgb = tuple(max(0, c - 30) for c in rgb)
            return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
        return color
    
    def on_enter(self, e):
        self.config(bg=self.hover_bg, cursor='hand2')
    
    def on_leave(self, e):
        self.config(bg=self.original_bg, cursor='')
    
    def on_click(self, e):
        self.config(relief=tk.SUNKEN)
        self.after(100, lambda: self.config(relief=tk.RAISED))


class DiscreteCalculatorApp:
    """Main GUI application for Discrete Structures Calculator."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Discrete Structures Calculator")
        self.root.geometry("1000x750")
        self.root.configure(bg="#f5f7fa")
        
        # Color scheme
        self.colors = {
            'primary': '#667eea',
            'secondary': '#764ba2',
            'success': '#27ae60',
            'danger': '#e74c3c',
            'warning': '#f39c12',
            'info': '#3498db',
            'purple': '#9b59b6',
            'dark': '#2c3e50',
            'light': '#ecf0f1',
            'bg': '#f5f7fa'
        }
        
        # Initialize modules
        self.number_converter = NumberSystemConverter()
        self.set_ops = SetOperations()
        self.search_algo = SearchingAlgorithms()
        self.sort_algo = SortingAlgorithms()
        
        self.create_widgets()
        self.setup_style()
    
    def setup_style(self):
        """Configure ttk styles."""
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TNotebook', background=self.colors['bg'], borderwidth=0)
        style.configure('TNotebook.Tab', padding=[20, 10], font=('Segoe UI', 10, 'bold'))
        style.map('TNotebook.Tab', background=[('selected', self.colors['primary'])], 
                  foreground=[('selected', 'white')])
    
    def create_widgets(self):
        """Create the main interface widgets."""
        # Header with gradient effect
        header = tk.Frame(self.root, bg=self.colors['primary'], height=80)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        # Title with shadow effect
        title_frame = tk.Frame(header, bg=self.colors['primary'])
        title_frame.pack(expand=True, fill=tk.BOTH)
        
        title_label = tk.Label(
            title_frame,
            text="🧮 Discrete Structures Calculator",
            font=("Segoe UI", 24, "bold"),
            bg=self.colors['primary'],
            fg="white"
        )
        title_label.pack(pady=20)
        
        subtitle = tk.Label(
            title_frame,
            text="Number Systems • Set Operations • Searching • Sorting",
            font=("Segoe UI", 10),
            bg=self.colors['primary'],
            fg="#e0e0e0"
        )
        subtitle.pack(pady=(0, 15))
        
        # Main container
        main_container = tk.Frame(self.root, bg=self.colors['bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Notebook for tabs
        self.notebook = ttk.Notebook(main_container)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs
        self.create_number_systems_tab()
        self.create_set_operations_tab()
        self.create_searching_tab()
        self.create_sorting_tab()
    
    def create_card_frame(self, parent, title):
        """Create a modern card-style frame."""
        card = tk.Frame(parent, bg='white', relief=tk.FLAT, bd=0)
        card.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Add shadow effect with border
        shadow = tk.Frame(parent, bg='#d0d0d0', height=2)
        shadow.pack(fill=tk.X, padx=12, pady=(0, 2))
        
        if title:
            title_label = tk.Label(
                card,
                text=title,
                font=("Segoe UI", 14, "bold"),
                bg='white',
                fg=self.colors['dark'],
                anchor='w'
            )
            title_label.pack(fill=tk.X, padx=20, pady=(15, 10))
        
        return card
    
    def create_number_systems_tab(self):
        """Create number systems conversion tab."""
        frame = ttk.Frame(self.notebook, padding=0)
        self.notebook.add(frame, text="🔢 Number Systems")
        
        # Input card
        input_card = self.create_card_frame(frame, "📥 Input")
        input_container = tk.Frame(input_card, bg='white')
        input_container.pack(fill=tk.X, padx=20, pady=15)
        
        # Number input
        tk.Label(input_container, text="Number:", font=("Segoe UI", 11, "bold"), 
                bg='white', fg=self.colors['dark']).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.num_input = tk.Entry(input_container, font=("Segoe UI", 12), width=35, 
                                  relief=tk.SOLID, bd=1, highlightthickness=2, 
                                  highlightcolor=self.colors['primary'], highlightbackground='#ddd')
        self.num_input.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.num_input.bind('<Return>', lambda e: self.convert_number())
        
        # From base
        tk.Label(input_container, text="From Base:", font=("Segoe UI", 11, "bold"), 
                bg='white', fg=self.colors['dark']).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.from_base = ttk.Combobox(input_container, values=["2 (Binary)", "8 (Octal)", "10 (Decimal)", "16 (Hexadecimal)"], 
                                      state="readonly", width=32, font=("Segoe UI", 11))
        self.from_base.set("10 (Decimal)")
        self.from_base.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        
        # To base
        tk.Label(input_container, text="To Base:", font=("Segoe UI", 11, "bold"), 
                bg='white', fg=self.colors['dark']).grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.to_base = ttk.Combobox(input_container, values=["2 (Binary)", "8 (Octal)", "10 (Decimal)", "16 (Hexadecimal)"], 
                                    state="readonly", width=32, font=("Segoe UI", 11))
        self.to_base.set("2 (Binary)")
        self.to_base.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        
        input_container.columnconfigure(1, weight=1)
        
        # Convert button
        btn_frame = tk.Frame(input_card, bg='white')
        btn_frame.pack(pady=15)
        convert_btn = ModernButton(btn_frame, text="🔄 Convert", command=self.convert_number, 
                                    bg=self.colors['primary'], fg="white", 
                                    font=("Segoe UI", 12, "bold"), padx=40, pady=12,
                                    relief=tk.RAISED, bd=0, cursor='hand2')
        convert_btn.pack()
        
        # Output card
        output_card = self.create_card_frame(frame, "📊 Result")
        output_container = tk.Frame(output_card, bg='white')
        output_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)
        
        self.num_result = scrolledtext.ScrolledText(
            output_container, height=12, font=("Consolas", 11), wrap=tk.WORD,
            bg='#fafafa', fg='#2c3e50', relief=tk.FLAT, bd=0, padx=15, pady=15,
            highlightthickness=1, highlightbackground='#ddd'
        )
        self.num_result.pack(fill=tk.BOTH, expand=True)
    
    def create_set_operations_tab(self):
        """Create set operations tab."""
        frame = ttk.Frame(self.notebook, padding=0)
        self.notebook.add(frame, text="📊 Set Operations")
        
        # Input card
        input_card = self.create_card_frame(frame, "📥 Input Sets")
        input_container = tk.Frame(input_card, bg='white')
        input_container.pack(fill=tk.X, padx=20, pady=15)
        
        tk.Label(input_container, text="Set A:", font=("Segoe UI", 11, "bold"), 
                bg='white', fg=self.colors['dark']).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.set_a_input = tk.Entry(input_container, font=("Segoe UI", 11), width=40,
                                    relief=tk.SOLID, bd=1, highlightthickness=2,
                                    highlightcolor=self.colors['primary'], highlightbackground='#ddd')
        self.set_a_input.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.set_a_input.insert(0, "1, 2, 3")
        
        tk.Label(input_container, text="Set B:", font=("Segoe UI", 11, "bold"), 
                bg='white', fg=self.colors['dark']).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.set_b_input = tk.Entry(input_container, font=("Segoe UI", 11), width=40,
                                    relief=tk.SOLID, bd=1, highlightthickness=2,
                                    highlightcolor=self.colors['primary'], highlightbackground='#ddd')
        self.set_b_input.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.set_b_input.insert(0, "2, 3, 4")
        
        input_container.columnconfigure(1, weight=1)
        
        # Operations buttons
        ops_frame = tk.Frame(input_card, bg='white')
        ops_frame.pack(pady=20)
        
        buttons = [
            ("Union (A ∪ B)", "union", self.colors['success']),
            ("Intersection (A ∩ B)", "intersection", self.colors['danger']),
            ("Difference (A - B)", "difference", self.colors['warning']),
            ("Cardinality", "cardinality", self.colors['purple'])
        ]
        
        for text, op, color in buttons:
            btn = ModernButton(ops_frame, text=text, command=lambda o=op: self.perform_set_op(o),
                              bg=color, fg="white", font=("Segoe UI", 10, "bold"),
                              padx=15, pady=10, relief=tk.RAISED, bd=0, cursor='hand2')
            btn.pack(side=tk.LEFT, padx=8)
        
        # Output card
        output_card = self.create_card_frame(frame, "📊 Result")
        output_container = tk.Frame(output_card, bg='white')
        output_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)
        
        self.set_result = scrolledtext.ScrolledText(
            output_container, height=12, font=("Consolas", 11), wrap=tk.WORD,
            bg='#fafafa', fg='#2c3e50', relief=tk.FLAT, bd=0, padx=15, pady=15,
            highlightthickness=1, highlightbackground='#ddd'
        )
        self.set_result.pack(fill=tk.BOTH, expand=True)
    
    def create_searching_tab(self):
        """Create searching algorithms tab."""
        frame = ttk.Frame(self.notebook, padding=0)
        self.notebook.add(frame, text="🔍 Searching")
        
        # Input card
        input_card = self.create_card_frame(frame, "📥 Input")
        input_container = tk.Frame(input_card, bg='white')
        input_container.pack(fill=tk.X, padx=20, pady=15)
        
        tk.Label(input_container, text="Array:", font=("Segoe UI", 11, "bold"), 
                bg='white', fg=self.colors['dark']).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.search_array_input = tk.Entry(input_container, font=("Segoe UI", 11), width=40,
                                           relief=tk.SOLID, bd=1, highlightthickness=2,
                                           highlightcolor=self.colors['primary'], highlightbackground='#ddd')
        self.search_array_input.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.search_array_input.insert(0, "2, 5, 8, 12, 16, 23, 38, 45, 56")
        
        tk.Label(input_container, text="Target:", font=("Segoe UI", 11, "bold"), 
                bg='white', fg=self.colors['dark']).grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.target_input = tk.Entry(input_container, font=("Segoe UI", 11), width=40,
                                     relief=tk.SOLID, bd=1, highlightthickness=2,
                                     highlightcolor=self.colors['primary'], highlightbackground='#ddd')
        self.target_input.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.target_input.insert(0, "23")
        
        input_container.columnconfigure(1, weight=1)
        
        # Search buttons
        search_frame = tk.Frame(input_card, bg='white')
        search_frame.pack(pady=20)
        
        linear_btn = ModernButton(search_frame, text="🔎 Linear Search", 
                                 command=lambda: self.perform_search("linear"),
                                 bg=self.colors['info'], fg="white", 
                                 font=("Segoe UI", 11, "bold"), padx=25, pady=12,
                                 relief=tk.RAISED, bd=0, cursor='hand2')
        linear_btn.pack(side=tk.LEFT, padx=10)
        
        binary_btn = ModernButton(search_frame, text="🎯 Binary Search", 
                                 command=lambda: self.perform_search("binary"),
                                 bg=self.colors['warning'], fg="white", 
                                 font=("Segoe UI", 11, "bold"), padx=25, pady=12,
                                 relief=tk.RAISED, bd=0, cursor='hand2')
        binary_btn.pack(side=tk.LEFT, padx=10)
        
        # Output card
        output_card = self.create_card_frame(frame, "📊 Result")
        output_container = tk.Frame(output_card, bg='white')
        output_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)
        
        self.search_result = scrolledtext.ScrolledText(
            output_container, height=12, font=("Consolas", 11), wrap=tk.WORD,
            bg='#fafafa', fg='#2c3e50', relief=tk.FLAT, bd=0, padx=15, pady=15,
            highlightthickness=1, highlightbackground='#ddd'
        )
        self.search_result.pack(fill=tk.BOTH, expand=True)
    
    def create_sorting_tab(self):
        """Create sorting algorithms tab."""
        frame = ttk.Frame(self.notebook, padding=0)
        self.notebook.add(frame, text="🔄 Sorting")
        
        # Input card
        input_card = self.create_card_frame(frame, "📥 Input")
        input_container = tk.Frame(input_card, bg='white')
        input_container.pack(fill=tk.X, padx=20, pady=15)
        
        tk.Label(input_container, text="Array:", font=("Segoe UI", 11, "bold"), 
                bg='white', fg=self.colors['dark']).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.sort_array_input = tk.Entry(input_container, font=("Segoe UI", 11), width=40,
                                        relief=tk.SOLID, bd=1, highlightthickness=2,
                                        highlightcolor=self.colors['primary'], highlightbackground='#ddd')
        self.sort_array_input.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.sort_array_input.insert(0, "64, 34, 25, 12, 22, 11, 90")
        
        input_container.columnconfigure(1, weight=1)
        
        # Sort buttons
        sort_frame = tk.Frame(input_card, bg='white')
        sort_frame.pack(pady=20)
        
        buttons = [
            ("🫧 Bubble Sort", "bubble", self.colors['danger']),
            ("🎯 Selection Sort", "selection", self.colors['success']),
            ("📥 Insertion Sort", "insertion", self.colors['purple'])
        ]
        
        for text, algo, color in buttons:
            btn = ModernButton(sort_frame, text=text, command=lambda a=algo: self.perform_sort(a),
                              bg=color, fg="white", font=("Segoe UI", 11, "bold"),
                              padx=20, pady=12, relief=tk.RAISED, bd=0, cursor='hand2')
            btn.pack(side=tk.LEFT, padx=10)
        
        # Output card
        output_card = self.create_card_frame(frame, "📊 Result")
        output_container = tk.Frame(output_card, bg='white')
        output_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)
        
        self.sort_result = scrolledtext.ScrolledText(
            output_container, height=12, font=("Consolas", 11), wrap=tk.WORD,
            bg='#fafafa', fg='#2c3e50', relief=tk.FLAT, bd=0, padx=15, pady=15,
            highlightthickness=1, highlightbackground='#ddd'
        )
        self.sort_result.pack(fill=tk.BOTH, expand=True)
    
    def animate_text(self, widget, text, delay=30):
        """Animate text insertion."""
        widget.delete(1.0, tk.END)
        for i, char in enumerate(text):
            widget.insert(tk.END, char)
            if i % 10 == 0:
                widget.update()
                time.sleep(delay / 1000)
    
    def convert_number(self):
        """Convert number between bases."""
        try:
            value = self.num_input.get().strip()
            from_base_str = self.from_base.get()
            to_base_str = self.to_base.get()
            
            if not value:
                messagebox.showerror("Error", "Please enter a number!")
                return
            
            # Extract base numbers
            base_map = {"2 (Binary)": 2, "8 (Octal)": 8, "10 (Decimal)": 10, "16 (Hexadecimal)": 16}
            from_base = base_map[from_base_str]
            to_base = base_map[to_base_str]
            
            result = self.number_converter.convert(value, from_base, to_base)
            
            self.num_result.delete(1.0, tk.END)
            output = f"╔════════════════════════════════════════╗\n"
            output += f"║  NUMBER SYSTEM CONVERSION RESULT      ║\n"
            output += f"╚════════════════════════════════════════╝\n\n"
            output += f"📥 Input:  {value} (Base {from_base})\n"
            output += f"📤 Output: {result} (Base {to_base})\n\n"
            output += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            output += f"📊 All Conversions:\n"
            output += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            
            for base_name, base_num in base_map.items():
                if base_num != from_base:
                    try:
                        conv_result = self.number_converter.convert(value, from_base, base_num)
                        output += f"  • {base_name:20s} → {conv_result}\n"
                    except:
                        pass
            
            self.num_result.insert(tk.END, output)
            self.num_result.see(tk.END)
        
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed: {str(e)}")
    
    def perform_set_op(self, operation):
        """Perform set operation."""
        try:
            set_a_str = self.set_a_input.get().strip()
            set_b_str = self.set_b_input.get().strip()
            
            if not set_a_str:
                messagebox.showerror("Error", "Please enter Set A!")
                return
            
            # Parse sets
            set_a = set(item.strip() for item in set_a_str.split(",") if item.strip())
            set_b = set(item.strip() for item in set_b_str.split(",") if item.strip()) if set_b_str else set()
            
            self.set_result.delete(1.0, tk.END)
            output = f"╔════════════════════════════════════════╗\n"
            output += f"║      SET OPERATION RESULT              ║\n"
            output += f"╚════════════════════════════════════════╝\n\n"
            output += f"📊 Set A: {set_a}\n"
            output += f"📊 Set B: {set_b}\n"
            output += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            
            if operation == "union":
                result = self.set_ops.union(set_a, set_b)
                output += f"✅ Union (A ∪ B): {result}\n"
            elif operation == "intersection":
                result = self.set_ops.intersection(set_a, set_b)
                output += f"✅ Intersection (A ∩ B): {result}\n"
            elif operation == "difference":
                result = self.set_ops.difference(set_a, set_b)
                output += f"✅ Difference (A - B): {result}\n"
            elif operation == "cardinality":
                output += f"✅ Cardinality of A (|A|): {self.set_ops.cardinality(set_a)}\n"
                if set_b:
                    output += f"✅ Cardinality of B (|B|): {self.set_ops.cardinality(set_b)}\n"
            
            self.set_result.insert(tk.END, output)
            self.set_result.see(tk.END)
        
        except Exception as e:
            messagebox.showerror("Error", f"Operation failed: {str(e)}")
    
    def perform_search(self, algorithm):
        """Perform search operation."""
        try:
            array_str = self.search_array_input.get().strip()
            target_str = self.target_input.get().strip()
            
            if not array_str:
                messagebox.showerror("Error", "Please enter an array!")
                return
            if not target_str:
                messagebox.showerror("Error", "Please enter a target value!")
                return
            
            # Parse array
            try:
                array = [int(x.strip()) for x in array_str.split(",") if x.strip()]
            except ValueError:
                array = [x.strip() for x in array_str.split(",") if x.strip()]
            
            # Parse target
            try:
                target = int(target_str.strip())
            except ValueError:
                target = target_str.strip()
            
            self.search_result.delete(1.0, tk.END)
            output = f"╔════════════════════════════════════════╗\n"
            output += f"║      SEARCH ALGORITHM RESULT          ║\n"
            output += f"╚════════════════════════════════════════╝\n\n"
            output += f"📊 Array:  {array}\n"
            output += f"🎯 Target: {target}\n"
            output += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            
            if algorithm == "linear":
                result, steps = self.search_algo.linear_search(array, target)
                output += f"🔎 Linear Search Result:\n"
                if result != -1:
                    output += f"   ✅ Found at index: {result}\n\n"
                else:
                    output += f"   ❌ Not found in array\n\n"
                output += f"📝 Steps:\n"
                for step in steps:
                    output += f"   • {step}\n"
            
            elif algorithm == "binary":
                sorted_array = sorted(array)
                output += f"📊 Sorted Array: {sorted_array}\n\n"
                result, steps = self.search_algo.binary_search(sorted_array, target)
                output += f"🎯 Binary Search Result:\n"
                if result != -1:
                    output += f"   ✅ Found at index: {result}\n\n"
                else:
                    output += f"   ❌ Not found in array\n\n"
                output += f"📝 Steps:\n"
                for step in steps:
                    output += f"   • {step}\n"
            
            self.search_result.insert(tk.END, output)
            self.search_result.see(tk.END)
        
        except Exception as e:
            messagebox.showerror("Error", f"Search failed: {str(e)}")
    
    def perform_sort(self, algorithm):
        """Perform sort operation."""
        try:
            array_str = self.sort_array_input.get().strip()
            
            if not array_str:
                messagebox.showerror("Error", "Please enter an array!")
                return
            
            # Parse array
            try:
                array = [int(x.strip()) for x in array_str.split(",") if x.strip()]
            except ValueError:
                array = [x.strip() for x in array_str.split(",") if x.strip()]
            
            self.sort_result.delete(1.0, tk.END)
            output = f"╔════════════════════════════════════════╗\n"
            output += f"║      SORTING ALGORITHM RESULT         ║\n"
            output += f"╚════════════════════════════════════════╝\n\n"
            output += f"📥 Original Array: {array}\n"
            output += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            
            if algorithm == "bubble":
                sorted_array, steps = self.sort_algo.bubble_sort(array.copy())
                output += f"🫧 Bubble Sort Result: {sorted_array}\n\n"
                output += f"📝 Sorting Steps:\n"
                for i, step in enumerate(steps, 1):
                    output += f"   Step {i}: {step}\n"
            
            elif algorithm == "selection":
                sorted_array, steps = self.sort_algo.selection_sort(array.copy())
                output += f"🎯 Selection Sort Result: {sorted_array}\n\n"
                output += f"📝 Sorting Steps:\n"
                for i, step in enumerate(steps, 1):
                    output += f"   Step {i}: {step}\n"
            
            elif algorithm == "insertion":
                sorted_array, steps = self.sort_algo.insertion_sort(array.copy())
                output += f"📥 Insertion Sort Result: {sorted_array}\n\n"
                output += f"📝 Sorting Steps:\n"
                for i, step in enumerate(steps, 1):
                    output += f"   Step {i}: {step}\n"
            
            self.sort_result.insert(tk.END, output)
            self.sort_result.see(tk.END)
        
        except Exception as e:
            messagebox.showerror("Error", f"Sort failed: {str(e)}")


def main():
    """Main function to run the application."""
    root = tk.Tk()
    app = DiscreteCalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
                                                                                                     
