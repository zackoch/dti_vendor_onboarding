from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import Optional, InputRequired
from wtforms.fields.html5 import DateField
from wtforms.widgets.html5 import NumberInput


class PhoneField(StringField):
    def process_formdata(self, valuelist):
        self.data = [v.replace('-', '') for v in valuelist]
        super().process_formdata(self.data)


class ContractorForm(FlaskForm):
    # company info
    company_name = StringField('Company Name', validators=[InputRequired(message="Please input your company name")])
    street_address = StringField('Street Address')
    street_address_2 = StringField('Address Line 2')
    city = StringField('City')
    state = StringField('State / Province / Region')
    zip = StringField('Zip / Postal Code')
    phone = PhoneField('Phone Number')
    website = StringField('Website')

    # shipping address
    shipping_address_different = SelectField('Is your shipping address different from your mailing address?',
                                             choices=[('No', 'No'),
                                                      ('Yes', 'Yes')], default='No')

    shipping_address = StringField('Street Address')
    shipping_address_2 = StringField('Address Line 2')
    shipping_city = StringField('City')
    shipping_state = StringField('State / Province / Region')
    shipping_zip = StringField('Zip / Postal Code')

    # billing address
    billing_address_different = SelectField('Is your billing address different from your mailing address?',
                                            choices=[('No', 'No'),
                                                     ('Yes', 'Yes')], default='No')
    billing_address = StringField('Street Address')
    billing_address_2 = StringField('Address Line 2')
    billing_city = StringField('City')
    billing_state = StringField('State / Province / Region')
    billing_zip = StringField('Zip / Postal Code')

    # primary contact 1
    p1_contact_first_name = StringField('First Name',
                                        validators=[InputRequired(message='Please input your first name')])
    p1_contact_last_name = StringField('Last Name', validators=[InputRequired(message='Please input your last name')])
    p1_contact_title = StringField('Title')
    p1_email = StringField('Email Address', validators=[InputRequired(message='Please input your email address')])
    p1_work_phone = PhoneField('Work Number', validators=[InputRequired(message='Please input your work phone number')])
    p1_mobile_phone = PhoneField('Mobile Number')
    add_secondary_contact = SelectField('Would you like to add a secondary contact?',
                                        choices=[('No', 'No'),
                                                 ('Yes', 'Yes')])

    # primary contact 2
    p2_contact_first_name = StringField('First Name')
    p2_contact_last_name = StringField('Last Name')
    p2_contact_title = StringField('Title')
    p2_email = StringField('Email Address')
    p2_work_phone = PhoneField('Work Number')
    p2_mobile_phone = PhoneField('Mobile Number')

    # a/r contact 1
    ar_contact_first_name = StringField('First Name')
    ar_contact_last_name = StringField('Last Name')
    ar_contact_title = StringField('Title')
    ar_email = StringField('Email Address')
    ar_work_phone = PhoneField('Work Number')
    ar_mobile_phone = PhoneField('Mobile Number')

    # biz information
    biz_date_started = DateField('Date Business Started', format='%Y-%m-%d', validators=([Optional()]))
    biz_type = SelectField('Type of Business',
                           choices=[('C Corporation', 'C Corporation'), ('S Corporation', 'S Corporation'),
                                    ('Partnership', 'Partnership'), ('Proprietorship', 'Proprietorship'),
                                    ('LLC', 'LLC')])
    biz_contractor_lic = StringField('Contractor License Number')
    biz_ftin = StringField('Federal Tax Identification Number')
    biz_affiliate = SelectField('Is your firm an affiliate or subsidiary of any other firm?', choices=[('No', 'No'),
                                                                                                       ('Yes', 'Yes')])
    biz_affiliate_company_name = StringField('Parent Company Name')
    biz_affiliate_address = StringField('Street Address')
    biz_affiliate_street_address_2 = StringField('Address Line 2')
    biz_affiliate_city = StringField('City')
    biz_affiliate_state = StringField('State / Province / Region')
    biz_affiliate_zip = StringField('Zip / Postal Code')
    biz_installer_cities = TextAreaField('Please list the cities where you have installers')
    biz_disadvantaged = SelectField('Is your firm a Disadvantaged Business?', choices=[('No', 'No'),
                                                                                       ('Yes', 'Yes')])

    biz_disadvantaged_type_dobe = BooleanField(label='DOBE - Disability Owned')
    biz_disadvantaged_type_dvbe = BooleanField(label='DVBE - Disabled Veteran')
    biz_disadvantaged_type_mbe = BooleanField(label='MBE - Minority Business')
    biz_disadvantaged_type_wbe = BooleanField(label='WBE - Women Business')
    biz_lang = StringField('Languages Supported')
    biz_union = SelectField('Are you Union members?', choices=[('No', 'No'), ('Yes', 'Yes')])
    biz_union_name = StringField('Please list Union Name')
    biz_industries_served_commercial = BooleanField(label='Commercial')
    biz_industries_served_residential = BooleanField(label='Residential')
    biz_industries_served_government = BooleanField(label='Government')

    biz_services_data = BooleanField(label='Data Cabling')
    biz_services_voice = BooleanField(label='Voice Cabling')
    biz_services_fiber = BooleanField(label='Fiber Install')
    biz_services_security = BooleanField(label='Security')
    biz_services_electrical = BooleanField(label='Electrical')
    biz_services_wap = BooleanField(label="Wireless APs")
    biz_services_it = BooleanField(label='Local IT Services')
    biz_services_pos = BooleanField(label='Point of Sale')
    biz_services_iot = BooleanField(label='IoT Deployments')

    biz_services_other = StringField('Please list any other services you provide')
    biz_sub_electric = SelectField('Do you subcontract electrical?', choices=[('No', 'No'), ('Yes', 'Yes')])
    biz_tech_installed_routers = BooleanField(label='Routers')
    biz_tech_installed_switches = BooleanField(label='Switches')
    biz_tech_installed_servers = BooleanField(label='Servers')
    biz_tech_installed_pbx = BooleanField(label='PBX')
    biz_tech_installed_pos = BooleanField(label='POS')
    biz_tech_installed_waps = BooleanField(label='Wireless Access Points')
    biz_tech_installed_av = BooleanField(label='Audio / Video Equipment')
    biz_tech_installed_cctv = BooleanField(label='CCTV')
    biz_tech_installed_cisco_colab = BooleanField(label='Cisco Collaboration')
    biz_tech_installed_video_conf = BooleanField(label='Video Conferencing')
    biz_tech_installed_server = BooleanField(label='Server Storage / Memory')
    biz_tech_installed_pc = BooleanField(label='PC Storage / Memory')
    biz_tech_installed_netapp = BooleanField(label='NetApp Installations')
    biz_tech_installed_vlan = BooleanField(label='VLAN')
    biz_tech_installed_gpon = BooleanField(label='GPON')
    biz_tech_installed_ekahau = BooleanField(label='Ekahau')
    biz_tech_installed_switch = BooleanField(label='Ethernet Switch Configuration')
    biz_tech_installed_docsis = BooleanField(label='DOCSIS')

    biz_tech_installed_other = StringField('Please list any other devices your technicians have installed')
    biz_tech_laptops = SelectField('Can you provide technicians onsite with laptops?',
                                   choices=[('No', 'No'), ('Yes', 'Yes')])
    biz_tech_surveys = SelectField('Can your technicians complete RF Wireless coverage surveys?',
                                   choices=[('No', 'No'), ('Yes', 'Yes')])
    biz_tech_on_staff = SelectField('Number of technicians on staff', choices=[('1', '1'),
                                                                               ('2-5', '2-5'),
                                                                               ('5-10', '5-10'),
                                                                               ('10-25', '10-25'),
                                                                               ('25-50', '25-50'),
                                                                               ('50+', '50+')])
    biz_bicsi_rcdd = IntegerField("Number of BICSI / RCDD's on staff?", widget=NumberInput(min=0, max=1000),
                                  validators=([Optional()]))
    biz_testing_equipment = TextAreaField('What type of testing equipment do you use for data cabling and fiber?')

    # hourly rate
    biz_data_voice_fiber_rate = StringField('Data / Voice / Fiber')
    biz_electrical_rate = StringField('Electrical')
    biz_other = StringField('Other')
    biz_coverage_area = TextAreaField('Please describe your coverage area')
    biz_travel_without_charges = StringField('How far will your crews travel without travel charges?')
    biz_travel_with_negotiations = StringField('How far will your crews travel with prices negotiations')

    # associations & certifications
    biz_associations_bicsi = BooleanField(label='BICSI')
    biz_associations_comptia = BooleanField(label='CompTIA')
    biz_associations_foa = BooleanField(label='FOA')
    biz_associations_iscet = BooleanField(label='ISCET')
    biz_associations_neca = BooleanField(label='NECA')
    biz_associations_pmi = BooleanField(label='PMI')
    biz_associations_tpma = BooleanField(label='TPMA')

    biz_certifications_panduit = BooleanField(label='Panduit')
    biz_certifications_homaco = BooleanField(label='Homaco')
    biz_certifications_berk = BooleanField(label='Berk Tek')
    biz_certifications_amp = BooleanField(label='Amp')
    biz_certifications_chatsworth = BooleanField(label='Chatsworth')
    biz_certifications_mowhawk = BooleanField(label='Mowhawk')
    biz_certifications_siemon = BooleanField(label='Siemon')
    biz_certifications_avaya = BooleanField(label='Avaya')
    biz_certifications_comm = BooleanField(label='Comm Scope / Systimax')
    biz_certifications_ortronics = BooleanField(label='Ortronics')
    biz_certifications_corning = BooleanField(label='Corning')
    biz_certifications_belden = BooleanField(label='Belden')
    biz_certifications_leviton = BooleanField(label='Leviton')
    biz_certifications_great = BooleanField(label='Great Lakes')
    biz_certifications_hoffman = BooleanField(label='Hoffman')
    biz_certifications_hubbell = BooleanField(label='Hubbell')
    biz_certifications_mod = BooleanField(label='Mod Tap')
    biz_certifications_superior = BooleanField(label='Superior Essex')

    # references
    ref_1_company_name = StringField('Company Name')
    ref_1_desc = TextAreaField('Project / Services Work Description')
    ref_1_first_name = StringField('First Name')
    ref_1_last_name = StringField('Last Name')
    ref_1_phone = PhoneField('Phone Number')
    ref_1_email = StringField('Email Address')
    ref_1_contact = SelectField('May we contact this reference?', choices=[('Yes', 'Yes'),
                                                                           ('No', 'No')])
    ref_additional = SelectField('Would you like to add another reference?', choices=[('No', 'No'),
                                                                                      ('Yes', 'Yes')])
    ref_2_company_name = StringField('Company Name')
    ref_2_desc = TextAreaField('Project / Services Work Description')
    ref_2_first_name = StringField('First Name')
    ref_2_last_name = StringField('Last Name')
    ref_2_phone = PhoneField('Phone Number')
    ref_2_email = StringField('Email Address')
    ref_2_contact = SelectField('May we contact this reference?', choices=[('Yes', 'Yes'),
                                                                           ('No', 'No')])

    # insurance
    biz_insurance = SelectField('Do you have Commercial General Liability Coverage?', choices=[('No', 'No'),
                                                                                               ('Yes', 'Yes')])
    biz_limits = StringField('Current Limits per Occurrence')
    biz_aggregate = StringField('Aggregate')
    biz_workers_comp = SelectField('Do you have Workers Compensation Coverage', choices=[('No', 'No'),
                                                                                         ('Yes', 'Yes')])
    biz_limits_accident = StringField('Current Limits per Accident')
    biz_disease = StringField('Disease Policy Limit')
    biz_disease_each_employee = StringField('Disease Each Employee')

    # i hate forms
    submit = SubmitField('Submit')
