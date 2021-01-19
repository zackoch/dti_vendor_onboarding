from datetime import datetime
from vendor_onboarding import db


class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # main address
    company_name = db.Column(db.Text)
    street_address = db.Column(db.Text)
    street_address_2 = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    zip = db.Column(db.Text)
    phone = db.Column(db.Text)
    website = db.Column(db.Text)

    # shipping address

    shipping_address = db.Column(db.Text)
    shipping_address_2 = db.Column(db.Text)
    shipping_city = db.Column(db.Text)
    shipping_state = db.Column(db.Text)
    shipping_zip = db.Column(db.Text)

    # billing address

    billing_address = db.Column(db.Text)
    billing_address_2 = db.Column(db.Text)
    billing_city = db.Column(db.Text)
    billing_state = db.Column(db.Text)
    billing_zip = db.Column(db.Text)

    # primary contact 1
    p1_contact_first_name = db.Column(db.Text)
    p1_contact_last_name = db.Column(db.Text)
    p1_contact_title = db.Column(db.Text)
    p1_email = db.Column(db.Text)
    p1_work_phone = db.Column(db.Text)
    p1_mobile_phone = db.Column(db.Text)

    # primary contact 2
    p2_contact_first_name = db.Column(db.Text)
    p2_contact_last_name = db.Column(db.Text)
    p2_contact_title = db.Column(db.Text)
    p2_email = db.Column(db.Text)
    p2_work_phone = db.Column(db.Text)
    p2_mobile_phone = db.Column(db.Text)

    # a/r contact 1
    ar_contact_first_name = db.Column(db.Text)
    ar_contact_last_name = db.Column(db.Text)
    ar_contact_title = db.Column(db.Text)
    ar_email = db.Column(db.Text)
    ar_work_phone = db.Column(db.Text)
    ar_mobile_phone = db.Column(db.Text)

    # biz information
    biz_date_started = db.Column(db.Text)
    biz_type = db.Column(db.Text)
    biz_contractor_lic = db.Column(db.Text)
    biz_ftin = db.Column(db.Text)
    biz_affiliate = db.Column(db.Text)
    biz_affiliate_company_name = db.Column(db.Text)
    biz_affiliate_address = db.Column(db.Text)
    biz_affiliate_street_address_2 = db.Column(db.Text)
    biz_affiliate_city = db.Column(db.Text)
    biz_affiliate_state = db.Column(db.Text)
    biz_affiliate_zip = db.Column(db.Text)
    biz_installer_cities = db.Column(db.Text)
    biz_disadvantaged = db.Column(db.Text)

    biz_disadvantaged_type_dobe = db.Column(db.Boolean)
    biz_disadvantaged_type_dvbe = db.Column(db.Boolean)
    biz_disadvantaged_type_mbe = db.Column(db.Boolean)
    biz_disadvantaged_type_wbe = db.Column(db.Boolean)
    biz_lang = db.Column(db.Text)
    biz_union = db.Column(db.Text)
    biz_union_name = db.Column(db.Text)
    biz_industries_served_commercial = db.Column(db.Boolean)
    biz_industries_served_residential = db.Column(db.Boolean)
    biz_industries_served_government = db.Column(db.Boolean)

    biz_services_data = db.Column(db.Boolean)
    biz_services_voice = db.Column(db.Boolean)
    biz_services_fiber = db.Column(db.Boolean)
    biz_services_security = db.Column(db.Boolean)
    biz_services_electrical = db.Column(db.Boolean)
    biz_services_wap = db.Column(db.Boolean)
    biz_services_it = db.Column(db.Boolean)
    biz_services_pos = db.Column(db.Boolean)
    biz_services_iot = db.Column(db.Boolean)

    biz_services_other = db.Column(db.Text)
    biz_sub_electric = db.Column(db.Text)
    biz_tech_installed_routers = db.Column(db.Boolean)
    biz_tech_installed_switches = db.Column(db.Boolean)
    biz_tech_installed_servers = db.Column(db.Boolean)
    biz_tech_installed_pbx = db.Column(db.Boolean)
    biz_tech_installed_pos = db.Column(db.Boolean)
    biz_tech_installed_waps = db.Column(db.Boolean)
    biz_tech_installed_av = db.Column(db.Boolean)
    biz_tech_installed_cctv = db.Column(db.Boolean)
    biz_tech_installed_cisco_colab = db.Column(db.Boolean)
    biz_tech_installed_video_conf = db.Column(db.Boolean)
    biz_tech_installed_server = db.Column(db.Boolean)
    biz_tech_installed_pc = db.Column(db.Boolean)
    biz_tech_installed_netapp = db.Column(db.Boolean)
    biz_tech_installed_vlan = db.Column(db.Boolean)
    biz_tech_installed_gpon = db.Column(db.Boolean)
    biz_tech_installed_ekahau = db.Column(db.Boolean)
    biz_tech_installed_switch = db.Column(db.Boolean)
    biz_tech_installed_docsis = db.Column(db.Boolean)

    biz_tech_installed_other = db.Column(db.Text)
    biz_tech_laptops = db.Column(db.Text)
    biz_tech_surveys = db.Column(db.Text)
    biz_tech_on_staff = db.Column(db.Text)
    biz_bicsi_rcdd = db.Column(db.Integer)
    biz_testing_equipment = db.Column(db.Text)

    # hourly rate
    biz_data_voice_fiber_rate = db.Column(db.Text)
    biz_electrical_rate = db.Column(db.Text)
    biz_other = db.Column(db.Text)
    biz_coverage_area = db.Column(db.Text)
    biz_travel_without_charges = db.Column(db.Text)
    biz_travel_with_negotiations = db.Column(db.Text)

    # associations & certifications
    biz_associations_bicsi = db.Column(db.Boolean)
    biz_associations_comptia = db.Column(db.Boolean)
    biz_associations_foa = db.Column(db.Boolean)
    biz_associations_iscet = db.Column(db.Boolean)
    biz_associations_neca = db.Column(db.Boolean)
    biz_associations_pmi = db.Column(db.Boolean)
    biz_associations_tpma = db.Column(db.Boolean)

    biz_certifications_panduit = db.Column(db.Boolean)
    biz_certifications_homaco = db.Column(db.Boolean)
    biz_certifications_berk = db.Column(db.Boolean)
    biz_certifications_amp = db.Column(db.Boolean)
    biz_certifications_chatsworth = db.Column(db.Boolean)
    biz_certifications_mowhawk = db.Column(db.Boolean)
    biz_certifications_siemon = db.Column(db.Boolean)
    biz_certifications_avaya = db.Column(db.Boolean)
    biz_certifications_comm = db.Column(db.Boolean)
    biz_certifications_ortronics = db.Column(db.Boolean)
    biz_certifications_corning = db.Column(db.Boolean)
    biz_certifications_belden = db.Column(db.Boolean)
    biz_certifications_leviton = db.Column(db.Boolean)
    biz_certifications_great = db.Column(db.Boolean)
    biz_certifications_hoffman = db.Column(db.Boolean)
    biz_certifications_hubbell = db.Column(db.Boolean)
    biz_certifications_mod = db.Column(db.Boolean)
    biz_certifications_superior = db.Column(db.Boolean)

    # references
    ref_1_company_name = db.Column(db.Text)
    ref_1_desc = db.Column(db.Text)
    ref_1_first_name = db.Column(db.Text)
    ref_1_last_name = db.Column(db.Text)
    ref_1_phone = db.Column(db.Text)
    ref_1_email = db.Column(db.Text)
    ref_1_contact = db.Column(db.Text)
    ref_2_company_name = db.Column(db.Text)
    ref_2_desc = db.Column(db.Text)
    ref_2_first_name = db.Column(db.Text)
    ref_2_last_name = db.Column(db.Text)
    ref_2_phone = db.Column(db.Text)
    ref_2_email = db.Column(db.Text)
    ref_2_contact = db.Column(db.Text)

    # insurance
    biz_insurance = db.Column(db.Text)
    biz_limits = db.Column(db.Text)
    biz_aggregate = db.Column(db.Text)
    biz_workers_comp = db.Column(db.Text)
    biz_limits_accident = db.Column(db.Text)
    biz_disease = db.Column(db.Text)
    biz_disease_each_employee = db.Column(db.Text)

    # admin
    form_payload = db.Column(db.JSON)
    qb_response = db.Column(db.JSON)
    submitted_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self,
                 company_name,
                 street_address,
                 street_address_2,
                 city,
                 state,
                 zip,
                 phone,
                 website,
                 shipping_address,
                 shipping_address_2,
                 shipping_city,
                 shipping_state,
                 shipping_zip,
                 billing_address,
                 billing_address_2,
                 billing_city,
                 billing_state,
                 billing_zip,
                 p1_contact_first_name,
                 p1_contact_last_name,
                 p1_contact_title,
                 p1_email,
                 p1_work_phone,
                 p1_mobile_phone,
                 p2_contact_first_name,
                 p2_contact_last_name,
                 p2_contact_title,
                 p2_email,
                 p2_work_phone,
                 p2_mobile_phone,
                 ar_contact_first_name,
                 ar_contact_last_name,
                 ar_contact_title,
                 ar_email,
                 ar_work_phone,
                 ar_mobile_phone,
                 biz_date_started,
                 biz_type,
                 biz_contractor_lic,
                 biz_ftin,
                 biz_affiliate,
                 biz_affiliate_company_name,
                 biz_affiliate_address,
                 biz_affiliate_street_address_2,
                 biz_affiliate_city,
                 biz_affiliate_state,
                 biz_affiliate_zip,
                 biz_installer_cities,
                 biz_disadvantaged,
                 biz_disadvantaged_type_dobe,
                 biz_disadvantaged_type_dvbe,
                 biz_disadvantaged_type_mbe,
                 biz_disadvantaged_type_wbe,
                 biz_lang,
                 biz_union,
                 biz_union_name,
                 biz_industries_served_commercial,
                 biz_industries_served_residential,
                 biz_industries_served_government,
                 biz_services_data,
                 biz_services_voice,
                 biz_services_fiber,
                 biz_services_security,
                 biz_services_electrical,
                 biz_services_wap,
                 biz_services_it,
                 biz_services_pos,
                 biz_services_iot,
                 biz_services_other,
                 biz_sub_electric,
                 biz_tech_installed_routers,
                 biz_tech_installed_switches,
                 biz_tech_installed_servers,
                 biz_tech_installed_pbx,
                 biz_tech_installed_pos,
                 biz_tech_installed_waps,
                 biz_tech_installed_av,
                 biz_tech_installed_cctv,
                 biz_tech_installed_cisco_colab,
                 biz_tech_installed_video_conf,
                 biz_tech_installed_server,
                 biz_tech_installed_pc,
                 biz_tech_installed_netapp,
                 biz_tech_installed_vlan,
                 biz_tech_installed_gpon,
                 biz_tech_installed_ekahau,
                 biz_tech_installed_switch,
                 biz_tech_installed_docsis,
                 biz_tech_installed_other,
                 biz_tech_laptops,
                 biz_tech_surveys,
                 biz_tech_on_staff,
                 biz_bicsi_rcdd,
                 biz_testing_equipment,
                 biz_data_voice_fiber_rate,
                 biz_electrical_rate,
                 biz_other,
                 biz_coverage_area,
                 biz_travel_without_charges,
                 biz_travel_with_negotiations,
                 biz_associations_bicsi,
                 biz_associations_comptia,
                 biz_associations_foa,
                 biz_associations_iscet,
                 biz_associations_neca,
                 biz_associations_pmi,
                 biz_associations_tpma,
                 biz_certifications_panduit,
                 biz_certifications_homaco,
                 biz_certifications_berk,
                 biz_certifications_amp,
                 biz_certifications_chatsworth,
                 biz_certifications_mowhawk,
                 biz_certifications_siemon,
                 biz_certifications_avaya,
                 biz_certifications_comm,
                 biz_certifications_ortronics,
                 biz_certifications_corning,
                 biz_certifications_belden,
                 biz_certifications_leviton,
                 biz_certifications_great,
                 biz_certifications_hoffman,
                 biz_certifications_hubbell,
                 biz_certifications_mod,
                 biz_certifications_superior,
                 ref_1_company_name,
                 ref_1_desc,
                 ref_1_first_name,
                 ref_1_last_name,
                 ref_1_phone,
                 ref_1_email,
                 ref_1_contact,
                 ref_2_company_name,
                 ref_2_desc,
                 ref_2_first_name,
                 ref_2_last_name,
                 ref_2_phone,
                 ref_2_email,
                 ref_2_contact,
                 biz_insurance,
                 biz_limits,
                 biz_aggregate,
                 biz_workers_comp,
                 biz_limits_accident,
                 biz_disease,
                 biz_disease_each_employee,
                 form_payload,
                 qb_response
                 ):
        # main address

        self.company_name = company_name
        self.street_address = street_address
        self.street_address_2 = street_address_2
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        self.website = website

        # shipping address

        self.shipping_address = shipping_address
        self.shipping_address_2 = shipping_address_2
        self.shipping_city = shipping_city
        self.shipping_state = shipping_state
        self.shipping_zip = shipping_zip

        # billing address

        self.billing_address = billing_address
        self.billing_address_2 = billing_address_2
        self.billing_city = billing_city
        self.billing_state = billing_state
        self.billing_zip = billing_zip

        # primary contact 1

        self.p1_contact_first_name = p1_contact_first_name
        self.p1_contact_last_name = p1_contact_last_name
        self.p1_contact_title = p1_contact_title
        self.p1_email = p1_email
        self.p1_work_phone = p1_work_phone
        self.p1_mobile_phone = p1_mobile_phone

        # primary contact 2

        self.p2_contact_first_name = p2_contact_first_name
        self.p2_contact_last_name = p2_contact_last_name
        self.p2_contact_title = p2_contact_title
        self.p2_email = p2_email
        self.p2_work_phone = p2_work_phone
        self.p2_mobile_phone = p2_mobile_phone

        # a/r contact 1

        self.ar_contact_first_name = ar_contact_first_name
        self.ar_contact_last_name = ar_contact_last_name
        self.ar_contact_title = ar_contact_title
        self.ar_email = ar_email
        self.ar_work_phone = ar_work_phone
        self.ar_mobile_phone = ar_mobile_phone

        # biz information

        self.biz_date_started = biz_date_started
        self.biz_type = biz_type
        self.biz_contractor_lic = biz_contractor_lic
        self.biz_ftin = biz_ftin
        self.biz_affiliate = biz_affiliate
        self.biz_affiliate_company_name = biz_affiliate_company_name
        self.biz_affiliate_address = biz_affiliate_address
        self.biz_affiliate_street_address_2 = biz_affiliate_street_address_2
        self.biz_affiliate_city = biz_affiliate_city
        self.biz_affiliate_state = biz_affiliate_state
        self.biz_affiliate_zip = biz_affiliate_zip
        self.biz_installer_cities = biz_installer_cities
        self.biz_disadvantaged = biz_disadvantaged
        self.biz_disadvantaged_type_dobe = biz_disadvantaged_type_dobe
        self.biz_disadvantaged_type_dvbe = biz_disadvantaged_type_dvbe
        self.biz_disadvantaged_type_mbe = biz_disadvantaged_type_mbe
        self.biz_disadvantaged_type_wbe = biz_disadvantaged_type_wbe
        self.biz_lang = biz_lang
        self.biz_union = biz_union
        self.biz_union_name = biz_union_name
        self.biz_industries_served_commercial = biz_industries_served_commercial
        self.biz_industries_served_residential = biz_industries_served_residential
        self.biz_industries_served_government = biz_industries_served_government
        self.biz_services_data = biz_services_data
        self.biz_services_voice = biz_services_voice
        self.biz_services_fiber = biz_services_fiber
        self.biz_services_security = biz_services_security
        self.biz_services_electrical = biz_services_electrical
        self.biz_services_wap = biz_services_wap
        self.biz_services_it = biz_services_it
        self.biz_services_pos = biz_services_pos
        self.biz_services_iot = biz_services_iot
        self.biz_services_other = biz_services_other
        self.biz_sub_electric = biz_sub_electric
        self.biz_tech_installed_routers = biz_tech_installed_routers
        self.biz_tech_installed_switches = biz_tech_installed_switches
        self.biz_tech_installed_servers = biz_tech_installed_servers
        self.biz_tech_installed_pbx = biz_tech_installed_pbx
        self.biz_tech_installed_pos = biz_tech_installed_pos
        self.biz_tech_installed_waps = biz_tech_installed_waps
        self.biz_tech_installed_av = biz_tech_installed_av
        self.biz_tech_installed_cctv = biz_tech_installed_cctv
        self.biz_tech_installed_cisco_colab = biz_tech_installed_cisco_colab
        self.biz_tech_installed_video_conf = biz_tech_installed_video_conf
        self.biz_tech_installed_server = biz_tech_installed_server
        self.biz_tech_installed_pc = biz_tech_installed_pc
        self.biz_tech_installed_netapp = biz_tech_installed_netapp
        self.biz_tech_installed_vlan = biz_tech_installed_vlan
        self.biz_tech_installed_gpon = biz_tech_installed_gpon
        self.biz_tech_installed_ekahau = biz_tech_installed_ekahau
        self.biz_tech_installed_switch = biz_tech_installed_switch
        self.biz_tech_installed_docsis = biz_tech_installed_docsis
        self.biz_tech_installed_other = biz_tech_installed_other
        self.biz_tech_laptops = biz_tech_laptops
        self.biz_tech_surveys = biz_tech_surveys
        self.biz_tech_on_staff = biz_tech_on_staff
        self.biz_bicsi_rcdd = biz_bicsi_rcdd
        self.biz_testing_equipment = biz_testing_equipment

        # hourly rate

        self.biz_data_voice_fiber_rate = biz_data_voice_fiber_rate
        self.biz_electrical_rate = biz_electrical_rate
        self.biz_other = biz_other
        self.biz_coverage_area = biz_coverage_area
        self.biz_travel_without_charges = biz_travel_without_charges
        self.biz_travel_with_negotiations = biz_travel_with_negotiations

        # associations & certifications

        self.biz_associations_bicsi = biz_associations_bicsi
        self.biz_associations_comptia = biz_associations_comptia
        self.biz_associations_foa = biz_associations_foa
        self.biz_associations_iscet = biz_associations_iscet
        self.biz_associations_neca = biz_associations_neca
        self.biz_associations_pmi = biz_associations_pmi
        self.biz_associations_tpma = biz_associations_tpma
        self.biz_certifications_panduit = biz_certifications_panduit
        self.biz_certifications_homaco = biz_certifications_homaco
        self.biz_certifications_berk = biz_certifications_berk
        self.biz_certifications_amp = biz_certifications_amp
        self.biz_certifications_chatsworth = biz_certifications_chatsworth
        self.biz_certifications_mowhawk = biz_certifications_mowhawk
        self.biz_certifications_siemon = biz_certifications_siemon
        self.biz_certifications_avaya = biz_certifications_avaya
        self.biz_certifications_comm = biz_certifications_comm
        self.biz_certifications_ortronics = biz_certifications_ortronics
        self.biz_certifications_corning = biz_certifications_corning
        self.biz_certifications_belden = biz_certifications_belden
        self.biz_certifications_leviton = biz_certifications_leviton
        self.biz_certifications_great = biz_certifications_great
        self.biz_certifications_hoffman = biz_certifications_hoffman
        self.biz_certifications_hubbell = biz_certifications_hubbell
        self.biz_certifications_mod = biz_certifications_mod
        self.biz_certifications_superior = biz_certifications_superior

        # references

        self.ref_1_company_name = ref_1_company_name
        self.ref_1_desc = ref_1_desc
        self.ref_1_first_name = ref_1_first_name
        self.ref_1_last_name = ref_1_last_name
        self.ref_1_phone = ref_1_phone
        self.ref_1_email = ref_1_email
        self.ref_1_contact = ref_1_contact
        self.ref_2_company_name = ref_2_company_name
        self.ref_2_desc = ref_2_desc
        self.ref_2_first_name = ref_2_first_name
        self.ref_2_last_name = ref_2_last_name
        self.ref_2_phone = ref_2_phone
        self.ref_2_email = ref_2_email
        self.ref_2_contact = ref_2_contact

        # insurance

        self.biz_insurance = biz_insurance
        self.biz_limits = biz_limits
        self.biz_aggregate = biz_aggregate
        self.biz_workers_comp = biz_workers_comp
        self.biz_limits_accident = biz_limits_accident
        self.biz_disease = biz_disease
        self.biz_disease_each_employee = biz_disease_each_employee

        # admin

        self.form_payload = form_payload
        self.qb_response = qb_response
