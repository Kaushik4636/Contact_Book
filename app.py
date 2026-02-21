import streamlit as st

# Initialize the contact book in session state so it doesn't disappear
if 'contact_book' not in st.session_state:
    st.session_state.contact_book = {}

st.set_page_config(page_title="Digital Contact Book", page_icon="📇")
st.title("📇 Digital Contact Book")

# Using tabs instead of a numbered menu for a better web feel
tab1, tab2, tab3 = st.tabs(["👥 View & Search", "➕ Add Contact", "⚙️ Manage"])

# --- Tab 1: View All Contacts ---
with tab1:
    st.header("Your Contacts")
    if not st.session_state.contact_book:
        st.info("No contacts yet. Go to the 'Add' tab to create one!")
    else:
        # Search bar for contacts
        search = st.text_input("Search by Name")
        for name, details in st.session_state.contact_book.items():
            if search.lower() in name.lower():
                with st.expander(f"👤 {name}"):
                    st.write(f"📞 **Phone:** {details['Phone']}")
                    st.write(f"📧 **Email:** {details['Email']}")

# --- Tab 2: Add New Contact ---
with tab2:
    st.header("Add New Entry")
    with st.form("add_form", clear_on_submit=True):
        new_name = st.text_input("Name")
        new_phone = st.text_input("Phone Number")
        new_email = st.text_input("Email Address")
        submit = st.form_submit_button("Save Contact")
        
        if submit:
            if new_name in st.session_state.contact_book:
                st.warning("Contact already exists!")
            elif new_name == "":
                st.error("Name cannot be empty.")
            else:
                st.session_state.contact_book[new_name] = {'Phone': new_phone, 'Email': new_email}
                st.success(f"Added {new_name}!")
                st.rerun() # Refresh to show in the list

# --- Tab 3: Manage (Update/Delete) ---
with tab3:
    st.header("Update or Delete")
    if not st.session_state.contact_book:
        st.write("Nothing to manage yet.")
    else:
        target = st.selectbox("Select a contact", list(st.session_state.contact_book.keys()))
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🗑️ Delete Contact", type="primary"):
                del st.session_state.contact_book[target]
                st.success(f"Deleted {target}")
                st.rerun()
        
        with col2:
            st.write("To update, simply delete and re-add or add logic here!")