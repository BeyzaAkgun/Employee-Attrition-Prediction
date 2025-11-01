package com.example.attrition;

import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;
import java.util.function.Predicate;
import java.util.regex.Pattern;

@Service
@AllArgsConstructor
public class EmailService implements Predicate<String> {
    private static final String EMAIL_REGEX =
            "^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$";

    private final Pattern pattern = Pattern.compile(EMAIL_REGEX);

    @Override
    public boolean test(String email) {
        if (email == null || email.trim().isEmpty()) {
            return false; // Return false for null or empty email
        }
        return pattern.matcher(email).matches();
    }
}
