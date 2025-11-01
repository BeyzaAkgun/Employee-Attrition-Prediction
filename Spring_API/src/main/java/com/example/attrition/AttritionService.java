package com.example.attrition;

import lombok.RequiredArgsConstructor;
import org.jetbrains.annotations.NotNull;
import org.springframework.stereotype.Service;

import java.util.Objects;
import java.util.Optional;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

@Service
@RequiredArgsConstructor
public class AttritionService {

    private final AttritionRepository attritionRepository;
    private final EmailService emailService;

    public void register(@NotNull HumanResources humanResources){
        boolean isValid = emailService.test(humanResources.getEmail());
        if(!isValid) throw new IllegalStateException("Email is not valid.");
        if(!checkPasswordPattern(humanResources.getPassword())){
            throw new IllegalStateException("Password must contain at least 8 characters, one uppercase letter, one lowercase letter, one digit and one special character (e.g., !@#$%^&*)");
        }
        Optional<HumanResources> HrByEmail = attritionRepository.findHrByEmail(humanResources.getEmail());
        if(HrByEmail.isPresent()){
            throw new IllegalStateException("Email taken");
        }
        attritionRepository.save(humanResources);
    }


    public boolean validation(String email, String password){
        Optional<HumanResources> humanResources = attritionRepository.findHrByEmail(email);
        return humanResources.isPresent() && Objects.equals(humanResources.get().getPassword(), password);
    }
    private boolean checkPasswordPattern(String password){
        String passwordPattern = "^(?=.*[a-zıçöşğü])(?=.*[A-ZÇÖŞĞÜİ])(?=.*\\d)(?=.*[@#$%^&!])[A-Za-zıçöşğüÇÖŞĞÜİ\\d@#$%^&!]{8,}$";
        Pattern pattern = Pattern.compile(passwordPattern);
        Matcher matcher = pattern.matcher(password);
        return matcher.matches();
    }

}
