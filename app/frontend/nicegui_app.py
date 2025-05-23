from nicegui import ui, app
import os
from datetime import datetime

# Configure the app
app.title = "AI Engineer Portfolio"
app.favicon = "🤖"

# Theme configuration
PRIMARY_COLOR = "#4F46E5"  # Indigo
SECONDARY_COLOR = "#10B981"  # Emerald
DARK_COLOR = "#1F2937"  # Dark gray
LIGHT_COLOR = "#F9FAFB"  # Light gray
TEXT_COLOR = "#111827"  # Near black

# Global styles
ui.add_head_html('''
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    :root {
        --primary: ''' + PRIMARY_COLOR + ''';
        --secondary: ''' + SECONDARY_COLOR + ''';
        --dark: ''' + DARK_COLOR + ''';
        --light: ''' + LIGHT_COLOR + ''';
        --text: ''' + TEXT_COLOR + ''';
    }
    
    body {
        font-family: 'Inter', sans-serif;
        color: var(--text);
        background-color: var(--light);
        scroll-behavior: smooth;
    }
    
    .section {
        padding: 4rem 0;
        scroll-margin-top: 4rem;
    }
    
    .section-title {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 2rem;
        color: var(--dark);
        border-bottom: 3px solid var(--primary);
        display: inline-block;
        padding-bottom: 0.5rem;
    }
    
    .card {
        border-radius: 0.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        background-color: white;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    }
    
    .skill-badge {
        background-color: var(--primary);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 9999px;
        font-weight: 500;
        display: inline-block;
        margin: 0.25rem;
    }
    
    .timeline-item {
        position: relative;
        padding-left: 2rem;
        padding-bottom: 2rem;
        border-left: 2px solid var(--primary);
    }
    
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -0.5rem;
        top: 0;
        width: 1rem;
        height: 1rem;
        border-radius: 50%;
        background-color: var(--primary);
    }
    
    .project-card {
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    
    .project-card-content {
        flex-grow: 1;
    }
    
    .navbar-link {
        color: white;
        text-decoration: none;
        padding: 0.5rem 1rem;
        border-radius: 0.25rem;
        transition: background-color 0.2s;
    }
    
    .navbar-link:hover {
        background-color: rgba(255, 255, 255, 0.1);
    }
    
    .contact-icon {
        font-size: 1.5rem;
        margin-right: 0.5rem;
        color: var(--primary);
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .section {
            padding: 2rem 0;
        }
        
        .section-title {
            font-size: 1.5rem;
        }
    }
</style>
''')

# Add viewport meta tag for responsiveness
ui.add_head_html('''
<meta name="viewport" content="width=device-width, initial-scale=1.0">
''')

# Data for the portfolio
portfolio_data = {
    'name': 'Alex Morgan',
    'title': 'AI Engineer & Machine Learning Specialist',
    'about': '''
    I'm an AI Engineer with expertise in machine learning, deep learning, and natural language processing.
    With over 5 years of experience building AI solutions for real-world problems, I specialize in developing
    scalable machine learning systems that deliver business value. My passion lies in creating AI that is
    not only powerful but also ethical, explainable, and accessible.
    ''',
    'skills': {
        'AI & ML': ['Machine Learning', 'Deep Learning', 'Natural Language Processing', 'Computer Vision', 'Reinforcement Learning'],
        'Programming': ['Python', 'TensorFlow', 'PyTorch', 'scikit-learn', 'Keras', 'JAX'],
        'Data': ['SQL', 'Pandas', 'NumPy', 'Data Visualization', 'Feature Engineering'],
        'MLOps': ['Docker', 'Kubernetes', 'CI/CD', 'Model Monitoring', 'ML Pipelines'],
        'Cloud': ['AWS SageMaker', 'Google Cloud AI', 'Azure ML', 'Vertex AI']
    },
    'projects': [
        {
            'title': 'Conversational AI Assistant',
            'description': 'Developed an advanced conversational AI system using transformer-based models with custom training on domain-specific data.',
            'technologies': ['PyTorch', 'Transformers', 'FastAPI', 'React'],
            'image': 'chatbot.jpg',
            'highlights': [
                'Achieved 92% user satisfaction rate',
                'Reduced customer service costs by 35%',
                'Implemented context-aware responses'
            ]
        },
        {
            'title': 'Computer Vision for Manufacturing',
            'description': 'Built a real-time defect detection system for manufacturing lines using computer vision and deep learning.',
            'technologies': ['TensorFlow', 'OpenCV', 'CUDA', 'Docker'],
            'image': 'computer_vision.jpg',
            'highlights': [
                'Reduced defect escape rate by 87%',
                'Processes 30 frames per second on edge devices',
                'Transfer learning approach for minimal training data'
            ]
        },
        {
            'title': 'Predictive Maintenance System',
            'description': 'Created an end-to-end predictive maintenance solution using IoT sensor data and machine learning to forecast equipment failures.',
            'technologies': ['scikit-learn', 'Time Series Analysis', 'AWS IoT', 'Grafana'],
            'image': 'predictive.jpg',
            'highlights': [
                'Prevented 15 critical failures in first quarter',
                'ROI of 300% within first year',
                'Anomaly detection with 94% accuracy'
            ]
        },
        {
            'title': 'NLP for Healthcare',
            'description': 'Developed a system to extract and structure information from medical records using advanced NLP techniques.',
            'technologies': ['spaCy', 'BERT', 'BioBERT', 'Flask'],
            'image': 'healthcare.jpg',
            'highlights': [
                'Reduced manual review time by 75%',
                'HIPAA-compliant processing pipeline',
                'Custom medical entity recognition models'
            ]
        }
    ],
    'experience': [
        {
            'role': 'Senior AI Engineer',
            'company': 'TechInnovate AI',
            'period': '2021 - Present',
            'description': 'Lead AI engineer responsible for developing and deploying machine learning solutions across multiple business units.',
            'achievements': [
                'Led a team of 5 ML engineers to deliver 3 major AI products',
                'Implemented MLOps practices reducing deployment time by 60%',
                'Designed company-wide AI strategy and best practices'
            ]
        },
        {
            'role': 'Machine Learning Engineer',
            'company': 'DataDriven Solutions',
            'period': '2018 - 2021',
            'description': 'Developed and deployed machine learning models for predictive analytics and natural language processing.',
            'achievements': [
                'Built recommendation engine increasing user engagement by 40%',
                'Created NLP pipeline for sentiment analysis with 87% accuracy',
                'Optimized ML models reducing inference time by 65%'
            ]
        },
        {
            'role': 'Data Scientist',
            'company': 'AnalyticsFirst',
            'period': '2016 - 2018',
            'description': 'Analyzed large datasets to extract insights and build predictive models for clients across industries.',
            'achievements': [
                'Developed churn prediction model saving $2M annually for a telecom client',
                'Created automated reporting system reducing manual work by 20 hours/week',
                'Mentored junior data scientists on ML best practices'
            ]
        }
    ],
    'education': [
        {
            'degree': 'M.S. in Computer Science, AI Specialization',
            'institution': 'Stanford University',
            'year': '2016'
        },
        {
            'degree': 'B.S. in Mathematics and Computer Science',
            'institution': 'MIT',
            'year': '2014'
        }
    ],
    'contact': {
        'email': 'alex.morgan@example.com',
        'linkedin': 'linkedin.com/in/alexmorgan',
        'github': 'github.com/alexmorgan',
        'twitter': 'twitter.com/alexmorgan_ai'
    }
}

# Create a responsive container for the entire application
@ui.page('/')
def portfolio_page():
    # Navigation bar
    with ui.header().classes('flex justify-between items-center p-4 bg-gray-900 text-white'):
        ui.label(portfolio_data['name']).classes('text-xl font-bold')
        
        # Desktop navigation
        with ui.element('div').classes('hidden md:flex space-x-4'):
            ui.link('About', '#about').classes('navbar-link')
            ui.link('Skills', '#skills').classes('navbar-link')
            ui.link('Projects', '#projects').classes('navbar-link')
            ui.link('Experience', '#experience').classes('navbar-link')
            ui.link('Contact', '#contact').classes('navbar-link')
        
        # Mobile navigation (hamburger menu)
        with ui.element('div').classes('md:hidden'):
            with ui.button(icon='menu', color='white').classes('bg-transparent'):
                with ui.menu().classes('bg-gray-900 text-white w-48'):
                    ui.link('About', '#about').classes('block p-2 hover:bg-gray-800')
                    ui.link('Skills', '#skills').classes('block p-2 hover:bg-gray-800')
                    ui.link('Projects', '#projects').classes('block p-2 hover:bg-gray-800')
                    ui.link('Experience', '#experience').classes('block p-2 hover:bg-gray-800')
                    ui.link('Contact', '#contact').classes('block p-2 hover:bg-gray-800')
    
    # Main content
    with ui.element('main').classes('container mx-auto px-4'):
        # Hero section
        with ui.element('section').classes('py-20 text-center'):
            ui.image('https://images.unsplash.com/photo-1591453089816-0fbb971b454c?auto=format&fit=crop&w=1200&h=400&q=80').classes('w-full h-64 object-cover rounded-lg mb-8')
            ui.label(portfolio_data['name']).classes('text-4xl font-bold mb-2')
            ui.label(portfolio_data['title']).classes('text-2xl text-gray-600 mb-6')
            with ui.element('div').classes('flex justify-center space-x-4'):
                ui.button('View Projects', on_click=lambda: ui.navigate('#projects')).classes('bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-3 rounded-lg')
                ui.button('Contact Me', on_click=lambda: ui.navigate('#contact')).classes('bg-gray-200 hover:bg-gray-300 text-gray-800 px-6 py-3 rounded-lg')
        
        # About section
        with ui.element('section').classes('section') as section:
            section.props('id=about')
            ui.label('About Me').classes('section-title')
            with ui.element('div').classes('grid grid-cols-1 md:grid-cols-3 gap-8'):
                with ui.element('div').classes('md:col-span-2'):
                    ui.markdown(portfolio_data['about']).classes('text-lg leading-relaxed')
                    
                    # Education
                    ui.label('Education').classes('text-xl font-semibold mt-6 mb-4')
                    for edu in portfolio_data['education']:
                        with ui.card().classes('mb-4'):
                            ui.label(edu['degree']).classes('text-lg font-medium')
                            ui.label(f"{edu['institution']} • {edu['year']}").classes('text-gray-600')
                
                with ui.card().classes('h-full flex flex-col justify-center items-center p-6'):
                    ui.image('https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=400&h=400&q=80').classes('w-48 h-48 rounded-full object-cover mb-4')
                    ui.label('AI Engineer').classes('text-lg font-medium')
                    ui.label('Passionate about solving complex problems with AI').classes('text-center text-gray-600')
        
        # Skills section
        with ui.element('section').classes('section bg-gray-50 py-16') as section:
            section.props('id=skills')
            with ui.element('div').classes('container mx-auto px-4'):
                ui.label('Skills & Expertise').classes('section-title')
                
                with ui.element('div').classes('grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6'):
                    for category, skills in portfolio_data['skills'].items():
                        with ui.card().classes('p-6'):
                            ui.label(category).classes('text-xl font-semibold mb-4 text-indigo-600')
                            with ui.element('div').classes('flex flex-wrap'):
                                for skill in skills:
                                    ui.label(skill).classes('skill-badge')
        
        # Projects section
        with ui.element('section').classes('section') as section:
            section.props('id=projects')
            ui.label('Featured Projects').classes('section-title')
            
            with ui.element('div').classes('grid grid-cols-1 md:grid-cols-2 gap-8'):
                for project in portfolio_data['projects']:
                    with ui.card().classes('project-card'):
                        # Use placeholder images from Unsplash
                        image_url = f"https://source.unsplash.com/random/800x600/?{project['image'].split('.')[0]}"
                        ui.image(image_url).classes('w-full h-48 object-cover rounded-t-lg')
                        
                        with ui.card_section().classes('project-card-content p-6'):
                            ui.label(project['title']).classes('text-xl font-semibold mb-2')
                            ui.label(project['description']).classes('text-gray-600 mb-4')
                            
                            ui.label('Technologies:').classes('font-medium mb-2')
                            with ui.element('div').classes('flex flex-wrap mb-4'):
                                for tech in project['technologies']:
                                    ui.label(tech).classes('bg-gray-200 text-gray-800 px-3 py-1 rounded-full text-sm mr-2 mb-2')
                            
                            ui.label('Key Highlights:').classes('font-medium mb-2')
                            with ui.element('ul').classes('list-disc pl-5'):
                                for highlight in project['highlights']:
                                    ui.element('li').classes('text-gray-600 mb-1').text(highlight)
        
        # Experience section
        with ui.element('section').classes('section bg-gray-50 py-16') as section:
            section.props('id=experience')
            with ui.element('div').classes('container mx-auto px-4'):
                ui.label('Professional Experience').classes('section-title')
                
                for job in portfolio_data['experience']:
                    with ui.card().classes('mb-8 timeline-item'):
                        ui.label(job['role']).classes('text-xl font-semibold')
                        ui.label(f"{job['company']} • {job['period']}").classes('text-indigo-600 mb-2')
                        ui.label(job['description']).classes('text-gray-600 mb-4')
                        
                        ui.label('Key Achievements:').classes('font-medium mb-2')
                        with ui.element('ul').classes('list-disc pl-5'):
                            for achievement in job['achievements']:
                                ui.element('li').classes('text-gray-600 mb-1').text(achievement)
        
        # Contact section
        with ui.element('section').classes('section') as section:
            section.props('id=contact')
            ui.label('Get In Touch').classes('section-title')
            
            with ui.element('div').classes('grid grid-cols-1 md:grid-cols-2 gap-8'):
                with ui.card().classes('p-6'):
                    ui.label('Contact Information').classes('text-xl font-semibold mb-4')
                    
                    with ui.element('div').classes('space-y-4'):
                        with ui.element('div').classes('flex items-center'):
                            ui.icon('email', size='lg').classes('contact-icon')
                            ui.link(portfolio_data['contact']['email'], f"mailto:{portfolio_data['contact']['email']}").classes('text-indigo-600 hover:underline')
                        
                        with ui.element('div').classes('flex items-center'):
                            ui.icon('link', size='lg').classes('contact-icon')
                            ui.link(portfolio_data['contact']['linkedin'], f"https://{portfolio_data['contact']['linkedin']}", new_tab=True).classes('text-indigo-600 hover:underline')
                        
                        with ui.element('div').classes('flex items-center'):
                            ui.icon('code', size='lg').classes('contact-icon')
                            ui.link(portfolio_data['contact']['github'], f"https://{portfolio_data['contact']['github']}", new_tab=True).classes('text-indigo-600 hover:underline')
                        
                        with ui.element('div').classes('flex items-center'):
                            ui.icon('chat', size='lg').classes('contact-icon')
                            ui.link(portfolio_data['contact']['twitter'], f"https://{portfolio_data['contact']['twitter']}", new_tab=True).classes('text-indigo-600 hover:underline')
                
                with ui.card().classes('p-6'):
                    ui.label('Send Me a Message').classes('text-xl font-semibold mb-4')
                    
                    name_input = ui.input('Your Name').classes('w-full mb-4')
                    email_input = ui.input('Your Email').classes('w-full mb-4')
                    subject_input = ui.input('Subject').classes('w-full mb-4')
                    message_input = ui.textarea('Message').classes('w-full mb-4').props('rows=5')
                    
                    def send_message():
                        if not name_input.value or not email_input.value or not message_input.value:
                            ui.notify('Please fill out all required fields', color='negative')
                            return
                        
                        # In a real application, this would send an email or store the message
                        ui.notify('Message sent successfully! I will get back to you soon.', color='positive')
                        name_input.value = ''
                        email_input.value = ''
                        subject_input.value = ''
                        message_input.value = ''
                    
                    ui.button('Send Message', on_click=send_message).classes('bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-2 rounded-lg')
    
    # Footer
    with ui.footer().classes('bg-gray-900 text-white py-8'):
        with ui.element('div').classes('container mx-auto px-4'):
            with ui.element('div').classes('grid grid-cols-1 md:grid-cols-3 gap-8'):
                with ui.element('div'):
                    ui.label(portfolio_data['name']).classes('text-xl font-bold mb-2')
                    ui.label(portfolio_data['title']).classes('text-gray-400')
                
                with ui.element('div'):
                    ui.label('Quick Links').classes('text-lg font-semibold mb-4')
                    with ui.element('div').classes('space-y-2'):
                        ui.link('About', '#about').classes('text-gray-400 hover:text-white block')
                        ui.link('Skills', '#skills').classes('text-gray-400 hover:text-white block')
                        ui.link('Projects', '#projects').classes('text-gray-400 hover:text-white block')
                        ui.link('Experience', '#experience').classes('text-gray-400 hover:text-white block')
                        ui.link('Contact', '#contact').classes('text-gray-400 hover:text-white block')
                
                with ui.element('div'):
                    ui.label('Connect').classes('text-lg font-semibold mb-4')
                    with ui.element('div').classes('flex space-x-4'):
                        ui.link('', f"mailto:{portfolio_data['contact']['email']}", new_tab=True).classes('text-gray-400 hover:text-white').props('icon=email')
                        ui.link('', f"https://{portfolio_data['contact']['linkedin']}", new_tab=True).classes('text-gray-400 hover:text-white').props('icon=link')
                        ui.link('', f"https://{portfolio_data['contact']['github']}", new_tab=True).classes('text-gray-400 hover:text-white').props('icon=code')
                        ui.link('', f"https://{portfolio_data['contact']['twitter']}", new_tab=True).classes('text-gray-400 hover:text-white').props('icon=chat')
            
            with ui.element('div').classes('mt-8 pt-8 border-t border-gray-800 text-center text-gray-400'):
                ui.label(f'© {datetime.now().year} {portfolio_data["name"]} • AI Engineer Portfolio')