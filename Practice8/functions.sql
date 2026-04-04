-- SEARCH FUNCTION (FIXED)
DROP FUNCTION IF EXISTS search_contacts(TEXT) CASCADE;

CREATE FUNCTION search_contacts(p_pattern TEXT)
RETURNS TABLE(name TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT c.name::TEXT, c.phone::TEXT
    FROM contacts c
    WHERE c.name ILIKE '%' || p_pattern || '%'
       OR c.phone ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;


-- PAGINATION FUNCTION (FIXED)
DROP FUNCTION IF EXISTS get_contacts_paginated(INT, INT) CASCADE;

CREATE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(name TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT c.name::TEXT, c.phone::TEXT
    FROM contacts c
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;